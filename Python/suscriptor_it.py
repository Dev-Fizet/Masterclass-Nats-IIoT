import importlib.util
import subprocess
import sys


def asegurar_dependencias():
    if importlib.util.find_spec("nats") is None:
        print("📦 Instalando 'nats-py' automáticamente...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "nats-py"])


asegurar_dependencias()

import asyncio
import json
import nats

SETPOINT_ALTA_TEMP = 88.0


async def main():
    nc = await nats.connect("nats://demo.nats.io:4222")
    print(f"🔵 [IT - Monitor Alertas] Escuchando telemetría (Set Point: {SETPOINT_ALTA_TEMP} °C)...")

    async def message_handler(msg):
        datos = json.loads(msg.data.decode())
        temp = datos["temperatura_c"]
        hora = datos["timestamp"]

        if temp >= SETPOINT_ALTA_TEMP:
            print(f"🚨 [ALERTA CRÍTICA - {hora}] Temperatura en {datos['equipo']}: {temp} °C (Supera Set Point)")
        else:
            print(f"✅ [OK - {hora}] {datos['equipo']} estable a {temp} °C | Nivel: {datos['nivel_pct']}%")

    await nc.subscribe("planta.linea1.reactor.telemetria", cb=message_handler)

    try:
        while True:
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        pass
    finally:
        await nc.close()


if __name__ == "__main__":
    asyncio.run(main())
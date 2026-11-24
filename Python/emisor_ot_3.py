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
import random
from datetime import datetime
import nats


async def main():
    nc = await nats.connect("nats://demo.nats.io:4222")
    print("🟢 [OT - PLC Simulador] Conectado a NATS. Enviando telemetría...")

    temperatura = 75.0
    nivel = 60.0

    try:
        while True:
            # Simulación de variación de proceso
            temperatura = round(temperatura + random.uniform(-1.5, 2.2), 2)
            if temperatura > 98.0:
                temperatura = 72.0  # Reinicio tras enfriamiento

            nivel = round(max(5.0, min(95.0, nivel + random.uniform(-2.0, 2.0))), 1)

            payload = {
                "timestamp": datetime.now().strftime("%H:%M:%S"),
                "equipo": "Reactor_03",
                "temperatura_c": temperatura,
                "nivel_pct": nivel,
                "bomba_activa": nivel > 90.0
            }

            mensaje = json.dumps(payload).encode()
            await nc.publish("planta.linea1.reactor.telemetria_3", mensaje)
            print(f"📤 Enviado: {payload}")
            await asyncio.sleep(1)

    except asyncio.CancelledError:
        pass
    finally:
        await nc.close()


if __name__ == "__main__":
    asyncio.run(main())
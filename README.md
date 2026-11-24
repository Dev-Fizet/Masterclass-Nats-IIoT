# El Sistema Nervioso de la Industria 4.0: Conectando OT e IT con NATS

Laboratorio práctico de una Masterclass para demostrar comunicación en tiempo real entre capas OT e IT mediante NATS. Los scripts Python simulan tres reactores industriales y un suscriptor muestra alertas según una temperatura límite.

## Arquitectura

- **NATS Server + JetStream:** recibe los mensajes publicados por los simuladores OT.
- **Emisores OT:** tres scripts Python que generan telemetría de temperatura y nivel.
- **Suscriptor IT:** recibe toda la telemetría y genera alertas cuando se supera el Set Point.
- **Node-RED:** interfaz HMI disponible en el puerto `1880`.

## Temas NATS

Cada emisor publica en un tema diferente:

- `planta.linea1.reactor.telemetria_1`
- `planta.linea1.reactor.telemetria_2`
- `planta.linea1.reactor.telemetria_3`

El suscriptor utiliza el wildcard `planta.linea1.reactor.telemetria_*` para escuchar los tres temas.

## Requisitos

- Python 3.10 o superior.

## Inicio rápido

pip install nats-py
```

Abre una terminal y ejecuta el suscriptor IT:

```bash
python Python/suscriptor_it.py
```

Abre una o tres terminales adicionales y ejecuta los emisores OT:

```bash
python Python/emisor_ot_1.py
python Python/emisor_ot_2.py
python Python/emisor_ot_3.py
```

Cada emisor publica una lectura por segundo. Para usar un servidor NATS remoto o diferente al local, define `NATS_URL`:

```bash
set NATS_URL=nats://SERVIDOR:4222
python Python/emisor_ot_1.py
```

En Linux o macOS:

```bash
NATS_URL=nats://SERVIDOR:4222 python Python/emisor_ot_1.py

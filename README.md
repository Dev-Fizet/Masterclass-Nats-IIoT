# El Sistema Nervioso de la Industria 4.0: Conectando OT e IT con NATS

Repositorio oficial con el laboratorio práctico de la Masterclass. Aquí encontrarás la infraestructura dockerizada y los scripts de simulación para probar mensajería de baja latencia en entornos industriales.

## Arquitectura del Laboratorio

* **NATS Server (JetStream):** Broker de mensajería y streaming de alta velocidad.
* **Emisor OT (Python):** Simulador de variables de proceso (temperatura, estado y nivel de tanque).
* **Suscriptor IT (Python):** Consumidor de eventos en tiempo real y disparador de alertas por Set Point.
* **Node-RED:** Interfaz HMI / Dashboard de visualización en tiempo real.

## Requisitos previos

* Docker y Docker Compose instalados.
* Python 3.10+ (si deseas correr los simuladores fuera de contenedores).

## Inicio rápido

1. Clona el repositorio:
   git clone https://github.com/tu-usuario/nats-industria40-lab.git
   cd nats-industria40-lab

2. Levanta los servicios:
   docker compose up -d

3. Accede a los paneles:
   * Monitoreo NATS: http://localhost:8222
   * Dashboard Node-RED: http://localhost:1880
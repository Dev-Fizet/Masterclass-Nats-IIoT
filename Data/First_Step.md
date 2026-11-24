# Primer paso: preparación del servidor

## Actualizar el servidor

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y ca-certificates curl
```

## Instalar Docker

```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER
newgrp docker
```

## Crear la infraestructura

Desde la carpeta donde se copiará el proyecto:

```bash
mkdir -p ~/masterclass-nats
cd ~/masterclass-nats
```

Crea el archivo `docker-compose.yml` de la raíz del repositorio o cópialo desde el proyecto:

```bash
docker compose up -d
docker compose ps
```

NATS estará disponible en:

- Clientes: `4222`
- Monitor HTTP: `8222`
- Node-RED: `1880`

## Preparar Python

```bash
sudo apt install -y python3-venv python3-pip
python3 -m venv venv
source venv/bin/activate
pip install nats-py
```

Ejecuta los programas desde la raíz del proyecto. Los scripts ya usan `nats://localhost:4222` por defecto.

Terminal 1:

```bash
source venv/bin/activate
python Python/suscriptor_it.py
```

Terminales adicionales:

```bash
source venv/bin/activate
python Python/emisor_ot_1.py
```

```bash
source venv/bin/activate
python Python/emisor_ot_2.py
```

```bash
source venv/bin/activate
python Python/emisor_ot_3.py
```

Para detener la infraestructura:

```bash
docker compose down
```

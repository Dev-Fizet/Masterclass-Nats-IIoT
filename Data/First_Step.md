First Step

Enable SSH en the software

make this in the server

-update server
sudo apt update && sudo apt upgrade -y
sudo apt install -y ca-certificates curl

-instal docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

-permision
sudo usermod -aG docker $USER
newgrp docker

-image docker

mkdir -p ~/masterclass-nats && cd ~/masterclass-nats
cat << 'EOF' > docker-compose.yml
services:
  nats:
    image: nats:latest
    container_name: nats-server
    command: "-js -m 8222"
    ports:
      - "4222:4222"   # Puerto de clientes (ESP32, Python, Node-RED)
      - "8222:8222"   # Puerto de monitoreo HTTP
    restart: unless-stopped

  nodered:
    image: nodered/node-red:latest
    container_name: nodered-hmi
    ports:
      - "1880:1880"
    depends_on:
      - nats
    restart: unless-stopped
EOF

-star server

docker compose up -d


-install python 

sudo apt install -y python3-venv python3-pip
python3 -m venv venv
source venv/bin/activate
pip install nats-py

cd ~/masterclass-nats && source venv/bin/activate && python suscriptor_it.py

cd ~/masterclass-nats && source venv/bin/activate && python emisor_ot.py
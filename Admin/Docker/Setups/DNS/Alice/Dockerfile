FROM debian:latest

RUN apt-get update && DEBIAN_FRONTEND=noninteractive && apt-get install -y \
    bind9 \
    dnsutils \
    iptables \
    tcpdump \
    python3 \
    python3-pip \
    vim

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .


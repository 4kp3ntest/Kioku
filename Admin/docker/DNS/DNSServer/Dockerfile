FROM debian:latest

RUN apt-get update && DEBIAN_FRONTEND=noninteractive && apt-get install -y \
    vim \
    bind9 \
    tcpdump \
    python3 \
    python3-pip \
    iptables 

COPY db.intra.domain.com /etc/bind/db.intra.domain.com
COPY named.conf.local /etc/bind/named.conf.local

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

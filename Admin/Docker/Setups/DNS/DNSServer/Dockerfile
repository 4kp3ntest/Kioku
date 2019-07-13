FROM debian:latest

RUN apt-get update && DEBIAN_FRONTEND=noninteractive && apt-get install -y \
    bind9 \
    dnsutils \
    iptables \
    tcpdump \
    python3 \
    python3-pip \
    vim

COPY db.rednet.badass /etc/bind/db.rednet.badass
COPY named.conf.local /etc/bind/named.conf.local
RUN /etc/init.d/bind9 restart

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

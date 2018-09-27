package: iptables
=================

# delete all rules
iptable -F
iptables -P INPUT DROP
iptables -P OUTPUT DROP
iptables -P FORWARD DROP
# list chains
iptables -L
iptables -L CHAIN --line-numbers
iptables -D CHAIN 1

# enable NAT
iptables -t nat -A POSTROUTING -o eth1 -j MASQUERADE
iptables -A FORWARD -i eth1 -o eth0 -j ACCEPT
iptables -A FORWARD -i eth0 -o eth1 -m state --state RELATED,ESTABLISHED -j ACCEPT

# ICMP
iptables -A OUTPUT -p icmp --icmp-type echo-request -j DROP
iptables -A INPUT -p icmp --icmp-type 8 -s 0/0 -d $SERVER_IP -m state --state NEW,ESTABLISHED,RELATED -j ACCEPT
iptables -A OUTPUT -p icmp --icmp-type 0 -s $SERVER_IP -d 0/0 -m state --state ESTABLISHED,RELATED -j ACCEPT
iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
iptables -A OUTPUT -p tcp -d 192.168.1.110 -s 192.168.1.1 --tcp-flags RST RST -j DROP
iptables -A FORWARD -i eth0 -o eth2 -s 192.168.1.0/24 -d 192.168.4.0/24 -j ACCEPT


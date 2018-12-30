package: iproute2
=================

# display
## all
ip -c a
## specific

# default GW/routes
## show, delete, add
ip route show
ip route del default
ip route add default via 172.18.0.2 dev eth0

# enable promisc mode
ip link set eth1 promisc on

ip link set name my_interface dev eth0

# change MAC address
[ip link set dev eth0 down]
ip link set dev eth0 address ff:ff:ff:ff:ff:ff
[ip link set dev eth0 up]



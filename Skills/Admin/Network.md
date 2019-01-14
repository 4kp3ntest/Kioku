package: iproute2
=================

# network devices under
/sys/class/net

# default GW/routes
## show, delete, add
ip route show
ip route del default
ip route add default via 172.18.0.2 dev eth0

# enable promisc mode
ip link set eth1 promisc on

# change MAC address
ip link set dev eth0 address ff:ff:ff:ff:ff:ff
macchanger -r device

### change name of interface
ip link set name my_interface dev eth0

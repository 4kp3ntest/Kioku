# autostart WIFI (wpa_actiond)
systemctl enalbe netctl-auto@wlan0.service

# network devices under
/sys/class/net

#package: iproute2 

# default GW/routes
## show, delete, add
ip route show
ip route del default
ip route add default via 172.18.0.2 dev eth0

# enable promisc mode
ip link set eth1 promisc on

# change address
### IP
ip addr add 192.168.1.111/24 dev wlp2s0
### MAC
ip link set dev eth0 address ff:ff:ff:ff:ff:ff
macchanger -r device

### change name of interface
ip link set name my_interface dev eth0

### delete interface
ip link delete

# connect to wifi and enable autostart
wifi-menu
pacman -S wpa_actiond avahi
systemctl enable netctl-auto@wlan0.service
systemctl enable avahi-daemon

# Set up new headless system to connect to wifi
## wpa_supplicant.conf
network={
               ssid="home"
               priority=1 # higher wins, default is 0
               psk="very secret passphrase"
          }

# DO NOT FORGET TO ADD HOOK TO /etc/network/interfaces
allow-hotplug wlan0
iface wlan0 inet dhcp
wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf

[wpa_cli select_network 1]

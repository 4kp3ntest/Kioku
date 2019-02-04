# Configure as Client
uci set network.lan.ipaddr='192.168.2.122'
uci set network.lan.gateway='192.168.2.1'
uci set network.lan.dns='192.168.2.1'
uci commit && service network restart 
# Package manager
opkg update
# Avahi - starts automatically it looks like
opkg install avahi-daemon-service-ssh

# Banner
vim /etc/banner


# Connect 
ssh root@OpenWrt.local

# Shutdown alternative
Openwrt uses reboot, halt or poweroff commands



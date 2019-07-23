# Package manager
opkg update
## Avahi - starts automatically
opkg install avahi-daemon-service-ssh
## NAS ext4 storage
opkg install kmod-usb-storage block-mount kmod-fs-ext4
## FTP Server
opkg install vsftpd

# Configure as Client
uci set network.lan.ipaddr='192.168.2.122'
uci set network.lan.gateway='192.168.2.1'
uci set network.lan.dns='192.168.2.1'
uci commit && service network restart 

# Start Services (OpenWrt uses init.d)
/etc/init.d/vsftpd enable
/etc/init.d/vsftpd start

# Connect 
ssh root@OpenWrt.local
# with entry in config
ssh oW

# Shutdown alternative
reboot, halt or poweroff


# MISC
## Banner
vim /etc/banner
## OpenWrt uses gluon for command line administration
https://github.com/freifunk-gluon/gluon/wiki/Commandline-administration

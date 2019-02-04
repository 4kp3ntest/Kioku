# set persistent keymap in /etc/vconsole.con
localectl set-keymap --no-convert de-latin1-nodeadkeys

# connect to wifi and enable autostart
wifi-menu
pacman -S wpa_actiond avahi
systemctl enalbe netctl-auto@wlan0.service
systemctl enable avahi-daemon

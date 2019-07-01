Bash stuff

#TODO kill all processes based on regex
# make außerdem einen count für bash functions/actions

# Important (conf) files and paths
/etc/pacman.conf
/etc/pacman.d/mirrorlist
/usr/share/doc/arch-wiki/html

apt-cache search something

# diff checksum
diff <(md5sum some_file.txt) <(echo 7393checksum#937)

# Write image to medium
dd bs=4M if=2018-04-18-raspbian-stretch.img of=/dev/sdX conv=fsync status=progress

# Add user to group
gpasswd -a user group


# list all setuid enabled files
find / -xdev \( -perm -4000 \) -type f -print0 | xargs -0 ls -l

# Shared folder
mount -t vboxsf -o uid=$UID,gid=$(id -g) Shared ~/host

# Start cups service to find printers in network (NOT WORKING)
systemctl start org.cups.cupsd.service

adb pull /storage/emulated/0/WhatsApp/Media/WhatsApp\ Images/
adb pull /storage/emulated/0/DCIM/Camera/

# MOST RECENT NEW COMMANDS

# Trust problem on kelevra
 pacman-key --init
 pacman-key --populate archlinuxarm

# Download content of webpage
wget -p -r -E -e robots=off --convert-links -U mozilla --level 1 some.site

# Generate QR code for Wifi
qrencode -o wifi.png "WIFI:S:Hive;T:WPA2;P:avIs7QqkRQ7QlsgBqbnI;;"

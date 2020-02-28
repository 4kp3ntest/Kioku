#!/bin/bash

#Two files need to be created to enable headless setup

echo '[INFO] Two files need to be created to enable headless setup'
echo '[INFO] ssh (empty) and wpa_supplicant.conf'
echo '[INFO] Both in /boot'
echo
echo '[!] Is pwd boot dir of sdcard? (y/n)'
read choice
if [[ $choice == 'y' ]]; then
    echo '\tCreating ssh file'
#   touch ssh
    echo '\tCreating wpa_supplicant.conf dummy'
    cat << EOF 
    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
    update_config=1
    country=GB
    
    network={
    	ssid="MrRobot"
    	psk="Far8rad8aY###"
    	priority=77
    }
EOF

else
    echo '\tDid nothing...'
fi




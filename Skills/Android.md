# connect via adb
adb connect host_ip:5555

# fastboot needs sudo!!!
fastboot flash bootloader some.img

# Routine to clean flash new Custom ROM
# Flash stock ROM
adb reboot bootloader
### execute flash_all script from stock ROM
sudo ./flash_all.sh

# Download TWRP and custom ROM and load ZIPs onto device
adb reboot bootloader
sudo fastboot boot twrp-installer.zip
## in TWRP - do NOT wipe anything between ROM installation and afterwards
Advanced wipe
Flash ROM with TWRP
Flash TWRP

# instructions here
https://forum.xda-developers.com/pixel/development/rom-pixel-dust-sailfish-t3585007
## Boot here
https://eu.dl.twrp.me/sailfish/
## Root here
https://forum.xda-developers.com/apps/magisk/official-magisk-v7-universal-systemless-t3473445

# Install .apk
adb install FDroid.apk

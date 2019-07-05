# ADB
## connect via adb
adb connect host_ip:5555

## Probably some backup routine soon
adb pull /storage/emulated/0/WhatsApp/Media/WhatsApp\ Images/
adb pull /storage/emulated/0/DCIM/Camera/

## Install .apk
adb install FDroid.apk


# Clean Flash (Custom ROM)
## Flash stock ROM
adb reboot bootloader
### execute flash_all script from stock ROM
sudo ./flash_all.sh

## Download TWRP and custom ROM and load ZIPs onto device
adb reboot bootloader
sudo fastboot boot twrp-installer.zip
#### in TWRP - do NOT wipe anything between ROM installation and afterwards
Advanced wipe
Flash ROM with TWRP
Flash TWRP


# More Instructions
https://forum.xda-developers.com/pixel/development/rom-pixel-dust-sailfish-t3585007

## Boot
https://eu.dl.twrp.me/sailfish/
### fastboot (sudo!)
fastboot flash bootloader some.img

## Root
https://forum.xda-developers.com/apps/magisk/official-magisk-v7-universal-systemless-t3473445


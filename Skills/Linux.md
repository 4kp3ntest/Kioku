# File Overview

## etc
login.defs
hosts
    -> name resolution for DNS
resolv.conf
shadow
sysctl.conf
pacman.conf
pacman.d/mirrorlist
passwd

## var
log/syslog


# System Info

## Block Devices
lsblk

## CPU
lscpu
cat /proc/cpuinfo

## Enviroment Variables
printenv
sysctl -a

## File Descriptors
ls -la /proc/$$/fd

## Kernel
uname -a

## Memory Maps
cat /proc/self/maps

## PCI
lspci

## USB
lsusb

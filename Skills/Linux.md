# File Overview

## etc
login.defs
hosts
    name resolution
resolv.conf
shadow
sysctl.conf
passwd


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

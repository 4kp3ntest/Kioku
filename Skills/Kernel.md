# install LTS kernel
pacman -S linux-lts
(pacman -R linux) !!

## Grub should be updated to use the right vmlinz file (?)
grub-mkconfig -o /boot/grub/grub.cfg
### change entries in /boot/loader/entries/arch.conf  !!

##Dirty COW Kernels
    4.8.0-26.28 for Ubuntu 16.10
    4.4.0-45.66 for Ubuntu 16.04 LTS
    3.13.0-100.147 for Ubuntu 14.04 LTS
    3.2.0-113.155 for Ubuntu 12.04 LTS
    3.16.36-1+deb8u2 for Debian 8
    3.2.82-1 for Debian 7
    4.7.8-1 for Debian unstable



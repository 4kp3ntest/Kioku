# LTS kernel
pacman -S linux-lts
pacman -R linux
grub-mkconfig -o /boot/grub/grub.cfg
### change entries in /boot/loader/entries/arch.conf  !!



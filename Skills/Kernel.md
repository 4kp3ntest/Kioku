# install LTS kernel
pacman -S linux-lts
(pacman -R linux) !!

## Grub should be updated to use the right vmlinz file (?)
grub-mkconfig -o /boot/grub/grub.cfg
### change entries in /boot/loader/entries/arch.conf  !!



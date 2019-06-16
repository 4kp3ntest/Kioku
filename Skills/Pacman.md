# Update
pacman -Syu
# Remove with unused depending packages
pacman -Rs
# Remove and do not care of dependencies!
pacman -Rdd

# Query local database
pacman -Q
pacman -Qe
# locally installed
pacman -Qm
## list all associated files
pacman -Qql

# Search for package string in remote
pacman -Fs somestring

# For recursively removing orphans and their configuration files
pacman -Rns $(pacman -Qtdq)

# PGP keys
pacman-key --init
### arch ARM
pacman-key --populate archlinuxarm

# Arch Linux
## Basic Workflow
### Update
pacman -Syu
### Remove with unused depending packages
pacman -Rs
### Remove and do not care of dependencies!
pacman -Rdd

## Query local database
pacman -Q
pacman -Qe
### locally installed
pacman -Qm
### list all associated files
pacman -Qql

## Query remote database
pacman -Fs somestring

## Tricks
### recursively remov orphans and their configuration files
pacman -Rns $(pacman -Qtdq)

### Init PGP keys
pacman-key --init
pacman-key --populate archlinuxarm


# Debian
## Basic Workflow
apt update && apt upgrade
apt install pkg
apt remove pkg

## Search for available versions
apt list -a bash

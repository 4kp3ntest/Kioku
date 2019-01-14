# Update
pacman -Syu

# Remove with unused depending packages
pacman -Rs

# Query local database
pacman -Q
pacman -Qe
# locally installed
pacman -Qm
## list all associated files
pacman -Qql

# Search for package string in remote
pacman -Fs somestring

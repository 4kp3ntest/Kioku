# Update
pacman -Syu

# Remove with unused depending packages
pacman -Rs

# Query local database
pacman -Q
pacman -Qe

# Search for package string in remote
pacman -Fs somestring

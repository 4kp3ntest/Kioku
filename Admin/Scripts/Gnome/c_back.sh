#!/bin/bash

# Hardcoded Path to my walllpaper folder
# first command line arg $1 must specify the second part of absolut path like favs/badass_tux.jpg

loc="/home/1xBilder/wallpaper/"

gsettings set org.gnome.desktop.background draw-background false
gsettings set org.gnome.desktop.background picture-uri \
    file:///$loc$1
gsettings set org.gnome.desktop.background draw-background true


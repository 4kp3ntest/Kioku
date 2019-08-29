#!/bin/bash


file_path=$(gsettings get org.gnome.desktop.background picture-uri)
file_path=${file_path:8:-1}
count_slashes=$(grep -o "/" <<< $file_path | wc -l)
((count_slashes++))
file_name=$(echo $file_path | cut -d'/' -f$count_slashes)

true_path=$(find /home/1xBilder -name $file_name)


echo $true_path
echo -n $true_path | xclip -selection c

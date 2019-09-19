#!/bin/bash

wp_path='/home/1xBilder/wallpaper/favs/'
fc_path=$HOME'/Admin[bella]/Scripts/3xGnome/c_back.sh'

# create two arrays [my_array, indices]
mapfile -t my_array < <( ls $wp_path | sort -R | tail -10 )
indices=${!my_array[*]}

# change for the ten alt[0-9].sh the line that calls c_back.sh
for index in $indices;
do
    echo $fc_path favs/${my_array[$index]} > alt$index.sh
    echo $fc_path favs/${my_array[$index]}
done

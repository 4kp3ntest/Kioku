#!/bin/bash

# Script toogled die Position der drei Statusleisten Buttons zwischen links und rechts

# get pos
#button_pos=$( gsettings get org.gnome.desktop.wm.preferences button-layout )
#set_button="gsettings set org.gnome.desktop.wm.preferences button-layout"
#
#
## left side: "close,minimize,maximize:"
#if [[ $button_pos =~ \': ]];then
#    $set_button "close,minimize,maximize:"
#else
#    $set_button ":close,minimize,maximize"
#fi

if [ $(gsettings get org.gnome.desktop.background show-desktop-icons) == 'true' ];then
    gsettings set org.gnome.desktop.background show-desktop-icons false
else
    gsettings set org.gnome.desktop.background show-desktop-icons true
fi

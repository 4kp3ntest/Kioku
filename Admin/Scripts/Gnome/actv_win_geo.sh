#!/bin/bash

#writtes the window configuration of active window to /tmp/win_geo.txt
#also writtes it to clipboard

xwininfo -id $(xprop -root | awk '/_NET_ACTIVE_WINDOW\(WINDOW\)/{print $NF}') | tail -2 | head -1 | xargs > /tmp/win_geo.txt
#xwininfo -id $(xprop -root | awk '/_NET_ACTIVE_WINDOW\(WINDOW\)/{print $NF}') | tail -2 | head -1 | xargs | xclip -selection c


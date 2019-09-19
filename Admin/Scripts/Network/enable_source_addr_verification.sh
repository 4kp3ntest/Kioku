#!/bin/sh
#author’s name: Michael K Aboagye
#purpose of program: to enable reverse path filtering
#date: 7/02/18
#displays “enabling source address verification” on the screen
echo -n "Enabling source address verification…"
#Overwrites the value 0 to 1 to enable source address verification
echo 1 > /proc/sys/net/ipv4/conf/default/rp_filter
echo "completed"

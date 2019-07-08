#!/bin/bash

fname='lucid_alarm.sh'
fpath='/root/'

# First kill existing lucid_alarm.sh
systemctl list-units |grep ${fname} |cut -d " " -f 3 |xargs systemctl stop > /dev/null

# Check for right input format
if [[ ! $1 =~ [0-9]{2}:[0-9]{2} ]]; then
    echo [*] $0 usage xx:xx
    exit
fi

# Get hours and minutes 
hour=$(echo $1 | cut -d ':' -f 1)
minute=$(echo $1 | cut -d ':' -f 2)

# Another check
if [[ $hour > 24 ]] || [[ $minute > 60 ]]; then
    echo [*] Not a valid time!
fi

# Calculate 25 min before provided wake up time 
if [[ $minute < 25 ]]; then
    wake_time=$(($hour-1)):$(($minute+35))
else
    wake_time=$hour:$(($minute-25))
fi

# Run service
systemd-run --on-calendar="${wake_time}:00" ${fname}${fpath}

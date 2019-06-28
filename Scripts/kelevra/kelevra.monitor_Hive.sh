#!/bin/bash

name=$(date +%F)
path=/root/Palast/Captures/

tshark -i wlan1 -w $path$name.pcap

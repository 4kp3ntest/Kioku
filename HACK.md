TODO - detailed writedown of the first three Boxes: brainpan, fristileaks & HackInOS
TODO - Hacking the Art of Exploitation: prepare booksrc as C reference


nmap -PN -sA -vv -n -p1-1000 -T4 -oNmapACKScan.txt 117.X.X.X

# [NOT TESTED]
airmon-ng start $iface
airodump-ng $mon
#airodump-ng --bssid xx:xx:xx:xx:xx:xx -c 1-13 [--write WPA_crack_file] <wlp2s0-'MON'>
aireplay-ng --deauth 100 -a $some_MAC -c $other_MAC $mon"

# start snort [NOT TESTED]
snort -de -i vboxnet0 --daq-dir /usr/lib/daq -c /etc/snort/snort.conf -l /var/log/snort/


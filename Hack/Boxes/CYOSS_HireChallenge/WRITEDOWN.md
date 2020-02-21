#Boot up system
imported appliance file into virtualbox
##Note: zip should contain a checksum!
change network mode to Host-only adapter to boot (Ubuntu 32-bit System: kylektatarn-VirtualBox)
IP addresse (displayed with ip cmnd) 192.168.56.102/24
double check with nmap:
nmap -sP 192.168.56.1/24
-> does also show a different IP 192.168.56.103
settings in Virtual Box reveals a second network adapter

#port scans to enumerate services
##basic TCP scan iface1 (all ports)
nmap -sN 192.168.56.102 -p-
3306/tcp open|filtered mysql
## iface2
nmap -sN 192.168.56.103 -p-
80/tcp open  http
##basic UDP scan on common ports (all ports takes forever)
nmap -sU 192.168.56.103
finds a bunch!
68/udp   open|filtered dhcpc
69/udp   open|filtered tftp
631/udp  open|filtered ipp
5353/udp open|filtered zeroconf

#Banner grabing
## port 68
list standarized ports tells 
Bootstrap Protocol (BOOTP) Client; auch genutzt von DHCP
nmap check for port info tells me used by dhcpc
-> erstmal vernachlässigen 

## port 3306 - mysql
default port für mysql (mariaDB on linux)
3306/tcp open  mysql   MySQL 5.5.5-10.4.12-MariaDB
GitHub has a tag for 5.5.5-m3 with latest changes dating 10 YEARS back:
https://github.com/MariaDB/server/tree/mysql-5.5.5-m3

## port 631 - CUPS
Remote Code Injection vulnerability in CUPS
CUPS Filter Bash Environment Variable Code Injection (Shellshock)

## port 5353 zeroconf
mdns - not my best bet

# Check out webserver @192.168.56.103:80
## nikto to check for vulnerabilities and directories
nikto -C all -host $vulIP
only reveals a /icons/README file (does not help) 
** "name= $given_hint . $extension" ** 
webpage hints at a broadcast.pcap
connecting to TFTP server, getting the pcap with _get broadcast.pcap_

##Analyzing trace
0000   00 00 03 04 00 06 00 00 00 00 00 00 00 00 08 00   ................
0010   45 00 01 0a 52 9e 40 00 40 06 f5 30 c0 a8 38 67   E...R.@.@.õ0À¨8g
0020   c0 a8 38 67 e4 c4 23 82 c9 af 1d 35 be 20 aa 9b   À¨8gäÄ#.É¯.5¾ ª.
0030   80 18 01 56 f3 1b 00 00 01 01 08 0a 00 09 4f a8   ...Vó.........O¨
0040   00 09 4f a8 48 65 6c 6c 6f 20 74 6f 20 74 68 65   ..O¨Hello to the
0050   20 4f 72 64 65 72 2e 20 41 73 20 74 68 65 20 43    Order. As the C
0060   68 61 6e 63 65 6c 6c 6f 72 20 68 61 73 20 75 73   hancellor has us
0070   20 70 69 6e 6e 65 64 20 64 6f 77 6e 20 77 65 20    pinned down we 
0080   74 6f 20 0d 0a 20 66 69 6e 64 20 73 6f 6d 65 20   to .. find some 
0090   63 6f 75 6e 74 65 72 6d 65 61 73 75 72 65 73 20   countermeasures 
00a0   66 6f 72 20 6f 75 72 20 63 6f 6d 6d 75 6e 69 63   for our communic
00b0   61 74 69 6f 6e 73 20 61 6e 64 20 0d 0a 20 61 20   ations and .. a 
00c0   70 61 64 61 77 61 6e 20 73 75 67 67 65 73 74 65   padawan suggeste
00d0   64 20 63 6f 6e 6e 65 63 74 69 6f 6e 6c 65 73 73   d connectionless
00e0   20 63 6f 6e 6e 65 63 74 69 6f 6e 73 21 20 54 72    connections! Tr
00f0   79 20 74 68 61 74 21 20 53 65 65 20 79 6f 75 20   y that! See you 
0100   54 68 65 72 65 21 20 0d 0a 48 6f 73 74 3a 20 4f   There! ..Host: O
0110   62 69 2d 57 61 6e 0d 0a 0d 0a                     bi-Wan....

###-> connectionless: the only UDP packet
Glad you got my Message. **We have to follow the Path to 
flag1{9442e4e83c5050b04376cba48ee828a2407b7d4b}.**
See you there! May the Force be with you! Obi-Wan

###They noticed the trace - did they take precautions??
>> Master Windu be careful when communicating order
>> Somethings not quite right
>> Someone is probably eavesdropping
>> Apparently there is a wireshark running
>> Someone is following our stack
>> Obi-Wan out!
>> May the force be with you

## Reveals a Hostname and the first flag
Host: Obi-Wan
flag1{9442e4e83c5050b04376cba48ee828a2407b7d4b}

# -> require a PASSWORD!
##What's next?
I poked around TFTP server for things like Order.txt or order.xlsx but without luck
-> Having a hostname but no password begs for some Brute Force!
There's a CVE for the cups service that is running on port 631
It requires a username (Obi-Wan) and a password

##Run OpenVAS before - just to be sure




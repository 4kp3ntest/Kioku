# MOTHERS OF ALL
https://github.com/Hack-with-Github/Awesome-Hacking

## Attack on Docker Setup
https://i.blackhat.com/us-18/Thu-August-9/us-18-McGrew-An-Attacker-Looks-At-Docker-Approaching-Multi-Container-Applications-wp.pdf

TODO - defined/useful docker setups (Apache Server, Scapy, DVA) callable with aliases
TODO - Check vimrc use of real tabs in specific folder
TODO - execute script on shutdown DOES NOT WORK
       service in /usr/lib/systemd/system-shutdown/clean_gnome_home.shutdown
       script in /bin/clean_home
       should remove: .gdb_history, .python_history, .motto_aliases!
TODO - Lucy: save current pixel configuration -> dedicated function to restore
TODO - Python: relevant stuff make a Notebook rather than a .md file (Python.md)
TODO - Docker: declutter and extend Dockerfiles folder
TODO - Docker: evaluate Setups and discard flask-redis
TODO - Tridactyl: Add config to Kioku
TODO - Hack: writedown of the first three Boxes: brainpan, fristileaks & HackInOS
TODO - Kelevra: create own AP if no netctl profile available
TODO - do-nothing script https://jamielinux.com/docs/openssl-certificate-authority/introduction.html
TODO - Clean and add a working zshrc to Kioku
TODO - Python: add Ipython profiles to Kioku
        - Hack (abgespeckte Version von kalis module set)
TODO - System: when connected to VPN, local network not working (add iptables (?) )
TODO - System: set random MAC on boot
TODO - System: Externe Festplatte ausmisten
TODO - System: System Backup machen

# NOTES
## New Tools
ranger

## PHP
Content of GET & POST in dedicated variables
Was not able to make PHP reverse shell oneliner work - nc stops but no sign of traffic in wireshark

## Python 
Awesome new JupyterLap extends old notebook
Need to define some shortcuts to make it useful (already blacklistadd url)


# UpTo's
### Hacking the Art of Exploitation: prepare booksrc as C reference
### Do-nothing script https://jamielinux.com/docs/openssl-certificate-authority/introduction.html
### (learn sed)
http://www.grymoire.com/Unix/Sed.html#uh-4a 
### Docker NAT Setup
https://www.karlrupp.net/en/computer/nat_tutorial
### Next Step is to have some sort of firewall
https://wiki.archlinux.org/index.php/simple_stateful_firewall


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


### Mount qcow2 files
modprobe nbd
qemu-nbd --connect=/dev/nbd0 /path/to/qcow2file
mount /dev/nbd0p1 mnt


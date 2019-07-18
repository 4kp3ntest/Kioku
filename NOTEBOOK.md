# MOTHERS OF ALL
https://github.com/Hack-with-Github/Awesome-Hacking

TODO - track cura bug issue
TODO - execute script on shutdown 
       so far:
       service in /usr/lib/systemd/system-shutdown/clean_gnome_home.shutdown
       script in /bin/clean_home
TODO - for Python relevant stuff make a Notebook rather than a .md file (Python.md)
TODO - Lucy: save current pixel configuration -> will need dedicated function to restore
TODO - declutter and extend Dockerfiles folder
TODO - Evaluate Docker Setups and discard flask-redis
TODO - Extract and add Tridactyl config
TODO - detailed writedown of the first three Boxes: brainpan, fristileaks & HackInOS
TODO - Hacking the Art of Exploitation: prepare booksrc as C reference
TODO - Kelevra: create own AP if no netctl profile available


## PHP
Content of GET & POST in dedicated variables
Was not able to make PHP reverse shell oneliner work - nc stops but no sign of traffic in wireshark

## Python 
Awesome new JupyterLap extends old notebook
Need to define some shortcuts to make it useful (already blacklistadd url)




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


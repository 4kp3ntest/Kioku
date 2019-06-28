# All lvl in one VBox @
https://exploit.education/downloads
(login as levelxy, pw levelxy)

#level01 - 7.6.2019
## printenv, effective UID/GID, system, /usr/bin/env 
file /home/flag01/fla01 has SUID bit set -> make it execute /bin/getflag
Add new path to environment and use
use system("/usr/bin/env echo") to execute own echo file

#level02
## asprintf - print to allocated string
see level01

#level03 
## crontab that gets executed regulary
TODO - not cracked


#level04
## symlink
Vulnerable C code that prints content of argv[1] but restricts file of interest explicitly
Just create a symlink to get pw of flag04 saved in token 

#level05
## tar -xvzf backup -C /home/level05, ssh
Backup folder accessible by all -> extract to any writeable folder
(folder contains ssh key for flag05 account)

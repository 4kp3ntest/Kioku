#Add a new user with home (-m) and a login shell (-s)
useradd -m -G additional_groups -s login_shell username

#Add user to group
gpasswd -a user group

#List all groups of user
groups gnome

#All groups of system in
/etc/group

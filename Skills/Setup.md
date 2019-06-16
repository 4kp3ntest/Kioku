# Keyboard Layout
## ARCH 
localectl set-keymap --no-convert de-latin1-nodeadkeys #set persistent keymap in /etc/vconsole.con
## RASPIAN
raspi-config


# Change default shell
echo $SHELL
#### find path
which bash | zsh
#### change
chsh -s /usr/bin/zsh

# Oh-my-ZSH
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
(cp /usr/share/oh-my-zsh/zshrc ~/.zshrc)


#TODO - default config files

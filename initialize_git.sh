#!/bin/zsh

# Symlink to new specific aliases
ln -fs $HOME/Palast/Kioku/Configs/aliases/Git_aliases.txt $HOME/.motto_aliases

# Send Signal to all zsh shells to source additional aliases
ps -u "$(id -u)" -o pid -o command | while read -r pid args; do
    if [[ $args = zsh || $args = */bin/zsh ]]; then
        kill -USR1 "$pid"
    fi
done

$ADMIN/Scripts/Gnome/c_back.sh favs/git

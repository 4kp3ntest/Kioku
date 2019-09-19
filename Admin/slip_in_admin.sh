#!/bin/zsh

# Symlink to new specific aliases
rm $HOME/.motto_aliases
ln -s $ADMIN/Admin_aliases.txt $HOME/.motto_aliases

# Send Signal to all zsh shells to source additional aliases
ps -u "$(id -u)" -o pid -o command | while read -r pid args; do
    if [[ $args = zsh || $args = */bin/zsh ]]; then
        kill -USR1 "$pid"
    fi
done

$ADMIN/Scripts/3xGnome/c_back.sh favs/badass_tux.jpg

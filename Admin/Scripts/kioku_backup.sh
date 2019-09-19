#!/bin/zsh

#path to default shell!

cd $KIOKU
if [ `git ls-files -m -o` ]; then
    git add *
    git commit -m 'automatic update'
    git push
fi

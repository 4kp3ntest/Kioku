#TODO - check if path is right

echo Starting Setup Process...

# [SETUP VIM]
echo '[VIM] First install vim with YouCompleteMe Plugin'
echo '[VIM] Make sure you have gvim and python3 installed (press enter to continue)'
read
echo '[VIM] Do you want to substitute .vimrc with the one in this repo (y/n)'
read choice
if [[ $choice == 'y' ]]; then
    echo '\tRemoving old file if it exists'
    rm $HOME/.vimrc
    echo '\tCreating symlink to config in repo'
    ln -s $PWD/Configs/vimrc $HOME/.vimrc
else
    echo '\tDid nothing...'
fi

# [VUNDLE & YOUCOMPLETEME]
echo '[VIM] Do you want to clone Vundle? (y/n)'
read choice
if [[ $choice == 'y' ]]; then
    echo '\tclone Vundle.vim Git repo'
    git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
else
    echo '\tDid nothing...'
fi
echo '[VIM] Do you want to clone YouCompleteMe? (y/n)'
read choice
if [[ $choice == 'y' ]]; then
    echo '\tclone YouCompleteMe Git repo'
    git clone https://github.com/Valloric/YouCompleteMe.git ~/.vim/bundle/YouCompleteMe
else
    echo '\tDid nothing...'
fi
echo '[VIM] Do you want to install Plugins? (y/n)'
read choice
if [[ $choice == 'y' ]]; then
    echo '\tRun PluginInstall with vim'
    vim +PluginInstall +qall
else
    echo '\tDid nothing...'
fi
echo '[VIM] Do you want to compile YouCompleteMe? (y/n)'
read choice
if [[ $choice == 'y' ]]; then
    echo '\tChange into ~/.vim/bundle/YouCompleteMe'
    cd ~/.vim/bundle/YouCompleteMe
    echo '\tRecursively update submodules'
    git submodule update --init --recursive
    echo '\tExecute install.py'
    python3 install.py
else
    echo '\tDid nothing...'
fi


# [SETUP ZSH]
echo '[ZSH] Setup zsh shell with Oh-my-ZSH'
echo '[ZSH] Make sure you have zsh installed (press enter to continue)'
echo '[ZSH] Do you want to change the shell to zsh? (y/n)'
read choice
if [[ $choice == 'y' ]]; then
    echo '\tChange shell to /usr/bin/zsh'
    chsh -s /usr/bin/zsh
else
    echo '\tDid nothing...'
fi
echo '[ZSH] Do you want to clone Oh-my-ZSH? (y/n)'
if [[ $choice == 'y' ]]; then
    echo '\tCloning Oh-my-ZSH'
    sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/\
        oh-my-zsh/master/tools/install.sh)"
else
    echo '\tDid nothing...'
fi
echo '[ZSH] Do you want to substitute .zshrc with the one in this repo (y/n)'
read choice
if [[ $choice == 'y' ]]; then
    echo '\tRemoving old file if it exists'
    rm $HOME/.zshrc
    echo '\tCreating symlink to config in repo'
    ln -s $PWD/Configs/zshrc/zshrc $HOME/.zshrc
else
    echo '\tDid nothing...'
fi

# [SETUP TERMINATOR]
echo '[TERM] Setup terminator '
echo '[TERM] Make sure you have terminator installed (press enter to continue)'
read
echo '[TERM] Do you want to substitute terminator/config with the one in this repo (y/n)'
read choice
if [[ $choice == 'y' ]]; then
    echo '\tRemoving old file if it exists'
    rm $HOME/.config/terminator/config
    echo '\tCreating symlink to config in repo'
    ln -s $PWD/Configs/terminator_conf.txt $HOME/.config/terminator/config
else
    echo '\tDid nothing...'
fi

# [ALIASES SETUP]
echo '[TERM] Do you want to substitute .aliases with the one in this repo (y/n)'
read choice
if [[ $choice == 'y' ]]; then
    echo '\tRemoving old file if it exists'
    rm $HOME/.aliases
    echo '\tCreating symlink to config in repo'
    ln -s $PWD/Configs/aliases/aliases $HOME/.aliases
else
    echo '\tDid nothing...'
fi


echo Setup finished


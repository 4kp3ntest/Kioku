package: vim-runtime, gvim, vim-gtk on raspian
==========================
# Install vundle & YouCompleteMe
git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
git clone https://github.com/Valloric/YouCompleteMe.git ~/.vim/bundle/YouCompleteMe

# Syntax highlighting Jenkins [TODO]
#git clone git@github.com:martinda/Jenkinsfile-vim-syntax.git ~/.vim/bundle/Jenkinsfile-vim-syntax

#TODO add to .zshrc
#to use visudo not with vi (deinstalled)
export VISUAL=vim
export EDITOR="$VISUAL"


# install plugins in ~/.vimrc
:PluginInstall

# YouCompleteMe needs to be compiled after downloading
cd ~/.vim/bundle/YouCompleteMe
git submodule update --init --recursive
python3 install.py

# Tricks
## Source from within file
:source %
## Shared Clipboard on remote host
req:    vim with clipboard support (gvim/vim-gtk), xauth installed
add 'ForwardX11 yes, ForwardX11Trusted yes' to .ssh/config
(set clipboard=unnamedplus in .vimrc)


# Substitute
## everywhere
:%s/foo/bar/g
## in line range
:5,12s/foo/bar/g
## from current line to last
:.,$s/foo/bar/g

# Folding           -> :help usr_28
zfap                #works also in visual mode
zd                  #DELETE
zo                  #wieder ausklappen
zr                  #ALLE wieder ausklappen
zc                  #wieder einklappen
zm                  #ALLE wieder einklappen
zi                  #TOGGLE between folded and unfolded

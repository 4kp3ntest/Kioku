package: vim-runtime, gvim
==========================
# Install vundle & YouCompleteMe
git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
git clone https://github.com/Valloric/YouCompleteMe.git ~/.vim/bundle/YouCompleteMe

# install plugins in ~/.vimrc
:PluginInstall

# YouCompleteMe needs to be compiled after downloading
cd ~/.vim/bundle/YouCompleteMe
python3 install.py

# Source from within file
:source %

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

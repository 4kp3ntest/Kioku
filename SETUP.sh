
# [CONFIG]
rm $HOME/.vimrc
rm $HOME/.zshrc
rm $HOME/.config/terminator/config
#TODO check user to determine which Shell config and aliases to use
ln -s $PWD/Configs/zshrc/zshrc $HOME/.zshrc
ln -s $PWD/Configs/aliases/aliases $HOME/.aliases
ln -s $PWD/Configs/vimrc $HOME/.vimrc
ln -s $PWD/Configs/terminator_conf.txt $HOME/.config/terminator/config

# [VIM] Install vundle & YouCompleteMe
git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
git clone https://github.com/Valloric/YouCompleteMe.git ~/.vim/bundle/YouCompleteMe
#:PluginInstall
vim +PluginInstall +qall
# Compile YouCompleteMe
cd ~/.vim/bundle/YouCompleteMe
git submodule update --init --recursive
python3 install.py

# [ZSH] Change SHELL
chsh -s /usr/bin/zsh
# Oh-my-ZSH
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

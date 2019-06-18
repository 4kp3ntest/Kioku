
# [CONFIG]
cp Configs/zshrc ~/.zshrc
cp Configs/vimrc ~/.vimrc

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

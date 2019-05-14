
# [CONFIG]
cp Configs/zshrc ~/.zshrc
cp Configs/vimrc ~/.vimrc
cp Configs/ ~/.vimrc

# [VIM] Install vundle & YouCompleteMe
git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
git clone https://github.com/Valloric/YouCompleteMe.git ~/.vim/bundle/YouCompleteMe
# Compile YouCompleteMe
cd ~/.vim/bundle/YouCompleteMe
python3 install.py
vim +PluginInstall +qall
#:PluginInstall

# [ZSH] Change SHELL
chsh -s /usr/bin/zsh
# Oh-my-ZSH
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

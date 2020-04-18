#!/usr/bin/python3

import subprocess
import os

user = input('To make things easier for now, please input user setup is running for:\n')
if user == 'root':
    home = '/root' 
else:
    home = '/home/'+user
base = os.path.dirname(os.path.realpath(__file__))

repo_vimrc   = base+'/Configs/vimrc'
repo_zshrc   = base+'/Configs/zshrc/zshrc'
repo_aliases = base+'/Configs/aliases/aliases'
home_vimrc   = home+'/.vimrc'
home_zshrc   = home+'/.zshrc'
home_aliases = home+'/.aliases'


def main():
    #TODO determine OS
    if confirm_user('vim required?'):
        setup_vim()
    if confirm_user('setup zsh shell?'):
        setup_zsh()

def setup_zsh():
    """
    ATM function does four things - every action can be executed or skipped seperately
    1. Change Shell to zsh - confirm if step is neccessary or automatically done by step 2
    2. Install Oh-my-ZSH directly from git link
    3. softlink .zshrc from repo to user home
    4. softlink .aliases from repo to user home
    """
    print('[ZSH] Setup zsh shell with Oh-my-ZSH')
    if confirm_user('Change shell to zsh?'):
        subprocess.call('chsh -s /usr/bin/zsh', shell=True)
    if confirm_user('Clone Oh-my-ZSH?'):
        subprocess.call('sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"', shell=True)
    if confirm_user('Softlink .zshrc from this repo?'):
        create_softlink(repo_zshrc, home_zshrc)
    if confirm_user('Softlink .aliases from this repo?'):
        create_softlink(repo_aliases, home_aliases)


def setup_vim():
    """
    ATM function does three things - every action can be executed or skipped seperately
    1. softlink .vimrc from repo to user home
    2. Clone Vundle git repo into ~/.vim
    3. Install plugins
    """
    print('[VIM] Install vim with default theme installed via Vundle')
    if confirm_user('Softlink .vimrc from this repo?'):
        create_softlink(repo_vimrc, home_vimrc)
    if confirm_user('clone Vundle GitRepo?\nYou really should - otherwise you get permanent warnings starting vim!'):
        subprocess.call('git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim', shell=True)
    if confirm_user('Install Plugins?'):
        subprocess.call('vim +PluginInstall +qall', shell=True)
    

def create_softlink(src, dst):
    """
    Creates a softlink via linux process call
    src: source of the file to softlink
    dst: name of the created softlink
    USE ABSOLUTE PATHS FOR BOTH ARGUMENTS
    """
    try:
        #TODO check if it is a Symlink 
        os.remove(dst)
    except FileNotFoundError:
        pass
    subprocess.call(['ln', '-s', src, dst])


def confirm_user(msg):
    """
    Prints function parameter msg
    Reads input from user checking for confirmation 
    and returns True or False regarding
    """
    confirm = ['y','yes','ja','j','sure']
    print(msg)
    choice = input().lower()
    if choice in confirm:
        return True 
    else:
        return False






def setup_terminator():
    pass
"""
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
"""    


if __name__ == '__main__':
    main()

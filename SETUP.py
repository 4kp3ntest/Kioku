#!/usr/bin/python3

import subprocess
import getpass
import os


user = getpass.getuser()
#base = os.path.dirname(os.path.realpath(__file__))
base = '/home/Kioku'
home = '/home/{}'.format(user)
#TODO make a check if home directory is correct

repo_vimrc      = base+'/Configs/vimrc0x1'
repo_zshrc      = base+'/Configs/zshrc/zshrc'
repo_aliases    = base+'/Configs/aliases/aliases'
repo_terminator = base+'/Configs/terminator_conf.txt'
repo_xbindkeys  = base+'/Configs/xbindkeysrc'
home_vimrc      = home+'/.vimrc'
home_zshrc      = home+'/.zshrc'
home_aliases    = home+'/.aliases'
home_terminator = home+'/.config/terminator/config'
home_xbindkeys  = home+'/.xbindkeysrc'


def main():
    #TODO determine OS
    #TODO make more verbose
    if confirm_user('[*] Setup vim?'):
        setup_vim()
    if confirm_user('[*] Setup zsh shell?'):
        setup_zsh()
    if confirm_user('[*] Setup terminator?'):
        setup_terminator()
    if confirm_user('[*] Setup xbindkeys? Might require restart'):
        setup_xbindkeys()

def setup_zsh():
    """
    ATM function does four things - every action can be executed or skipped seperately
    1. Change Shell to zsh - confirm if step is neccessary or automatically done by step 2
    2. Install Oh-my-ZSH directly from git link
    3. softlink .zshrc from repo to user home
    4. softlink .aliases from repo to user home
    """
    print('[ZSH] Setup zsh shell with Oh-my-ZSH')
    # directory ~/.cache should exist
    try:
        os.makedirs(home+'/.cache')
    except FileExistsError:
        pass
    if confirm_user('Change shell to zsh?'):
        subprocess.call('chsh -s /usr/bin/zsh', shell=True)
    if confirm_user('Clone Oh-my-ZSH?'):
        subprocess.call('sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"', shell=True)
        #TODO process stops after Oh-my-ZSH changes shell
    if confirm_user('Softlink .zshrc from this repo?'):
        create_softlink(repo_zshrc, home_zshrc)
    if confirm_user('Softlink .aliases from this repo?'):
        create_softlink(repo_aliases, home_aliases)

def setup_xbindkeys():
    if confirm_user('Softlink .xbindkeys from this repo?'):
        create_softlink(repo_xbindkeys, home_xbindkeys)
    

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
    print('Copy Terminator config')
    if confirm_user('Softlink terminator config?'):
        try:
            os.makedirs(home+'/.config/terminator/')
        except FileExistsError:
            pass
        create_softlink(repo_terminator, home_terminator)
    else:
        pass


if __name__ == '__main__':
    main()

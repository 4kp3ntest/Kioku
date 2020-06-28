#!/usr/bin/python3

import subprocess
import getpass
import pwd
import os

"""
list of required packages for all features:
    vim-athena/vim-gtk3
    terminator
    zsh
    xbindkeys
"""


def recon():
    """
    Function checks which user runs the script
    If it is root the setup can be executed for additional users
    returns: a list of users
    """
    #TODO determine OS
    user = getpass.getuser()
    base = os.path.dirname(os.path.realpath(__file__))
    
    if base != '/home/Kioku':
        print('[!] Repository path should be /home/Kioku or everything collapses')
        print('[!] Exiting')
        exit()
    if user == 'root':
        print('[*] Initial Setup with user root user - AWESOME!')
        print('[*] Security implications inclusive')
        print('[*] You want to run setup for additional users? (Coma seperated list)')
        additional_users = input().split(',')
        user_list = ['root'] + additional_users
    else:
        user_list = [user]

    return user_list

def static_paths(user):
    """
    Function sets all paths required for the setup based on the user name submitted
    arg1: name of the user as str
    return: dictory of path to config files in repo and users home
    """
    if user == 'root':
        home = '/root'
    else:
        home = '/home/'+user
    paths = dict(
    home            = home,
    repo_vimrc      = '/home/Kioku/Configs/vimrc0x1',
    repo_zshrc      = '/home/Kioku/Configs/zshrc/zshrc',
    repo_aliases    = '/home/Kioku/Configs/aliases/aliases',
    repo_terminator = '/home/Kioku/Configs/terminator_conf.txt',
    repo_xbindkeys  = '/home/Kioku/Configs/xbindkeysrc',
    home_vimrc      = home+'/.vimrc',
    home_zshrc      = home+'/.zshrc',
    home_aliases    = home+'/.aliases',
    home_terminator = home+'/.config/terminator/config',
    home_xbindkeys  = home+'/.xbindkeysrc'
    )

    return paths

def set_process_ids(info):
    print(info)
    os.getuid
    os.setuid(info.pw_uid)
    os.getuid

def main():
    users = recon()
    for user in users:
        print('[*] Setup for user {}'.format(user))
        try:
            info = pwd.getpwnam(user)
        except KeyError:
            print("[!] User '{}' not valid - Skipping!".format(user)) 
            break

        #TODO find best solution to run multiple commands with lower priviledges without loosing root
        # At the moment only one additional user can be set up due to priviledge loss
        set_process_ids(info)

        #TODO make more verbose
        subprocess.call('id', shell=True)
        subprocess.call(['id'])
        paths = static_paths(user)
        if confirm_user('[*] Setup vim?'):
            setup_vim(paths['home'], paths['repo_vimrc'], paths['home_vimrc'])
        if confirm_user('[*] Setup zsh shell?'):
            setup_zsh(paths['home'], paths['repo_zshrc'], paths['home_zshrc'])
#                   paths['repo_aliases'], paths['home_aliases'])
        if confirm_user('[*] Setup terminator?'):
            setup_terminator(paths['home'], paths['repo_terminator'], paths['home_terminator'])
        if confirm_user('[*] Setup xbindkeys? Might require restart'):
            setup_xbindkeys(paths['repo_xbindkeys'], paths['home_xbindkeys'])


def setup_vim(home, repo_vimrc, home_vimrc):
    """
    Function does three things - every action can be executed or skipped seperately
    1. softlink .vimrc from repo to user home
    2. Clone Vundle git repo into ~/.vim
    3. Install plugins
    """
    print('[VIM] Install vim with default theme installed via Vundle')
    if confirm_user('Softlink .vimrc from this repo?'):
        create_softlink(repo_vimrc, home_vimrc)
    if confirm_user('clone Vundle GitRepo?\nYou really should - otherwise you get permanent warnings starting vim!'):
        subprocess.call('git clone https://github.com/VundleVim/Vundle.vim.git {}/.vim/bundle/Vundle.vim'.format(home), shell=True)
    if confirm_user('Install Plugins?'):
        subprocess.call('vim +PluginInstall +qall', shell=True)

def setup_aliases(repo_aliases, home_aliases):
    if confirm_user('Softlink .aliases from this repo?'):
        create_softlink(repo_aliases, home_aliases)

def setup_zsh(home, repo_zshrc, home_zshrc):
    """
    ATM function does four things - every action can be executed or skipped seperately
    1. Change Shell to zsh - confirm if step is neccessary or automatically done by step 2
    2. softlink .zshrc from repo to user home
    3. softlink .aliases from repo to user home
    4. Install Oh-my-ZSH directly from Git
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
        #TODO not sure what the oh-my-zsh installer uses to determine users home
        # It's not uid for that matter..
        subprocess.call('sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"', shell=True)
    if confirm_user('Softlink .zshrc from this repo?'):
        create_softlink(repo_zshrc, home_zshrc)

def setup_terminator(home, repo_terminator, home_terminator):
    print('Copy Terminator config')
    if confirm_user('Softlink terminator config?'):
        try:
            os.makedirs(home+'/.config/terminator/')
        except FileExistsError:
            pass
        create_softlink(repo_terminator, home_terminator)
    else:
        pass

def setup_xbindkeys(repo_xbindkeys, home_xbindkeys):
    if confirm_user('Softlink .xbindkeys from this repo?'):
        create_softlink(repo_xbindkeys, home_xbindkeys)

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


if __name__ == '__main__':
    main()

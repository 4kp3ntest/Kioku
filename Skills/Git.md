# Check if Gitlab uses same exact Syntax
git clone --recurse-submodules -j8 <some repo>

# Basic workflow 
git add (-n) *
git commit -m 'some message'
git push -u origin master

# Show all branches of repo
git branch -a
git checkout <full/branch/name>  -> DETACHED HEAD
git checkout <name>              -> Not detached head

# Merge develope into master
(master) git merge develope
git push

# Set Config
git config 
git config --list
git config user.name 'Mona Lisa'

# Set remote
#### to use SSH
git remote set-url origin git@github.com:skllrn/reponame.git
#### to use HTTPS
git remote set-url origin https://github.com/skllrn/Kioku

# Check remote
git remote -v
git remote show origin


# Test SSH keys
ssh -vT git@github.com


# Unrelated histories (if master is empty)
--allow-unrelated-histories


# Add submodule
git submodule add https://github.com/some/repo
##### info in .gitmodules
git submodule init
git submodule update 
##### or git pull in submodule toplevel


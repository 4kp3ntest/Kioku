# clone repo with all submodules
git clone --recurse-submodules -j8 $somerepo
## Add submodule
git submodule add https://github.com/some/repo
#### info in .gitmodules
git submodule init
git submodule update 
##### or git pull in submodule toplevel

# Basic workflow 
git add (-n) *
git commit -m 'some message'
git push -u origin master
## Revert file to older commit
git checkout c5f567 -- file/to/retore

# Branching
## Show (all) branches of repo
git branch -a
## Create new branch
git checkout -b myLocalBranch
## Checkout existing branches
TODO - why and what was the issue with detached head
git checkout /full/branch/name  -> DETACHED HEAD
git checkout name               -> No detached head

# Merge develope into master
(master) git merge develope
git push

# Set Config
git config 
git config --list
git config user.name 'skllrn'

# Remote
## Set remote SSH
git remote set-url origin git@github.com:skllrn/reponame.git
(e.g. git@git.pixel-group.local:mixed-mode-security/static-analysis.git)
### HTTPS
git remote set-url origin https://github.com/skllrn/Kioku
## Check remote
git remote -v
git remote show origin
## Test SSH keys
ssh -vT git@github.com

# Special flags
## Unrelated histories (if master is empty)
--allow-unrelated-histories


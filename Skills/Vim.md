package: vim-runtime, gvim
==========================

:source %

# install plugins in ~/.vimrc
:PluginInstall

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

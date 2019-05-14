# Autoload - put in startup file
get_ipython().magic(u"%reload_ext autoreload")
get_ipython().magic(u"%autoreload 2")

# Create a profile including ipython_config.py
ipython profile create MitM

# Change default editor in profile
ipython_qtconsole_config.py

# Magic commands
whos
save filename 1-xx (lines)
colors


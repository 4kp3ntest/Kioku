import time
import re
import os
import sys
from scapy.all import *
from scapy_ssl_tls.ssl_tls import *


## Imports for Padding Oracle Attack
#from Cryptodome.Cipher import AES
#from Cryptodome import Random


# Autoreload
get_ipython().magic(u"%reload_ext autoreload")
get_ipython().magic(u"%autoreload 2")

# Change color theme to differentiate mallory
get_ipython().magic(u"%colors LightBG")


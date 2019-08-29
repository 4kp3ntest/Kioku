import sys, os
import subprocess
import socket
import docker
import re
from hashlib import *

get_ipython().magic(u"%reload_ext autoreload")
get_ipython().magic(u"%autoreload 2")

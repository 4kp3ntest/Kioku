# Modules
boofuzz
pexpect
PIL
pip-autoremove
pwntools
pycryptodome
pytesseract
scapy
shutil

# Reminders ;)
## generators -> a ephemeral iterable (what yield returns)


# Jupyter
## generate config
jupyter notebook --generate-config
## Allow external IP (existing config file $HOME/.jupyter)
c.NotebookApp.allow_origin = '192.168.56.1'
c.NotebookApp.ip = '0.0.0.0' # listen on all IPs

# Venv
python -m venv testerix
### python2.7
virtualenv -p /usr/bin/python2.7 --clear venv_Host
source /venv/bin/activate
##create kernel for jupyter (venv needs to be active!)
pip install ipykernel
python -m ipykernel install --user --name=VenvName

# Ipython
## Create a profile
ipython profile create MitM
## Change default editor in profile [CONFIRM]
ipython_qtconsole_config.py
## Magic commands
whos
save filename 1-xx (lines)
colors
### Auto reload (put in startup file)
get_ipython().magic(u"%reload_ext autoreload")
get_ipython().magic(u"%autoreload 2")
## Debug
%debug 
import ipdb; ipdb.set_trace()




# Python magic
## Rotate integer
pwn.util.fiddling.rol - pwn.util.fiddling.ror
### Rotate left: 0b1001 --> 0b0011
rol = lambda val, r_bits, max_bits: \
    (val << r_bits%max_bits) & (2**max_bits-1) | \
    ((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))
### Rotate right: 0b1001 --> 0b1100
ror = lambda val, r_bits, max_bits: \
    ((val & (2**max_bits-1)) >> r_bits%max_bits) | \
    (val << (max_bits-(r_bits%max_bits)) & (2**max_bits-1))

## find longest matching substring
from difflib import SequenceMatcher
        match = SequenceMatcher(None, string1, string2)\
                .find_longest_match(0, len(string1), 0, len(string2))
        if match.size > match_min_len:
            match_min_len = match.size
            matches = [row]
        elif match.size == match_min_len:
            matches.append(row)

## Load excel sheet
import pandas as pd
xl = pd.ExcelFile(XLSX)
df0 = xl.parse(xl.sheet_names[0])
df0.to_csv('tmp0.txt')
with open('tmp0.txt') as fp:
    xlsx = fp.read()

## load string from image
import pytesseract
    im = Image.open(val[1])
    text = pytesseract.image_to_string(im, lang='eng')

## Awesome Regex
def reg_replace(m, i):
    return m.group().replace(m.groups()[0], "'{}'".format(i[3][0]))
reg = 'id == (' + str(i[0]) + ')[ \:]'
# Use lambda function to pass additional arg to re.sub function
output = re.sub(reg, lambda m: reg_replace(m, i), output)

## spoof user agent
from urllib.request import urlopen, Request

req = Request('http://www.debian.org')
req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64; 
  rv:24.0) Gecko/20140722 Firefox/24.0 Iceweasel/24.7.0')


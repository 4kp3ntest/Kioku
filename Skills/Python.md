# Modules
boofuzz
PIL
pwntools
pycryptodome
pytesseract
scapy


# Python magic

##Show all ports as open
from scapy.all import *
os.system("iptables -A OUTPUT -p tcp -o eth0 --sport 1:65535 
--tcp-flags RST RST -j DROP")
def packet(pkt):
    if pkt[TCP].flags == 2:
        print('SYN packet detected port : ' + str(pkt[TCP].sport) + 
        ' from IP Src : ' + pkt[IP].src)
        send(IP(dst=pkt[IP].src, src=pkt[IP].dst)/
        TCP(dport=pkt[TCP].sport, sport=pkt[TCP].dport,ack=pkt[TCP].seq + 1,
        flags='SA'))
sniff(iface="eth0", prn=packet, filter="tcp[0xd]&18=2",count=100)
os.system("iptables -D OUTPUT -p tcp -o eth0 --sport 1:65535 
--tcp-flags RST RST -j DROP")

## Rotate left: 0b1001 --> 0b0011
rol = lambda val, r_bits, max_bits: \
    (val << r_bits%max_bits) & (2**max_bits-1) | \
    ((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))
## Rotate right: 0b1001 --> 0b1100
ror = lambda val, r_bits, max_bits: \
    ((val & (2**max_bits-1)) >> r_bits%max_bits) | \
    (val << (max_bits-(r_bits%max_bits)) & (2**max_bits-1))

# find longest matching substring
from difflib import SequenceMatcher
        match = SequenceMatcher(None, string1, string2)\
                .find_longest_match(0, len(string1), 0, len(string2))
        if match.size > match_min_len:
            match_min_len = match.size
            matches = [row]
        elif match.size == match_min_len:
            matches.append(row)

# Load excel sheet
import pandas as pd
xl = pd.ExcelFile(XLSX)
df0 = xl.parse(xl.sheet_names[0])
df0.to_csv('tmp0.txt')
with open('tmp0.txt') as fp:
    xlsx = fp.read()

# load string from image
import pytesseract
    im = Image.open(val[1])
    text = pytesseract.image_to_string(im, lang='eng')

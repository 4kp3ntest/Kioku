# Normal scan: ping sweep, TCP scan
# Agnostic scan: -Pn

# Ping sweep
nmap -sP 192.168.1.1/24

# Check most used ports and try to determine Service running on open port
nmap -sV 192.168.1.100

## TESTOUT
nmap -v -sS -A -T4 target
nmap -PN -sA -vv -n -p1-1000 -T4 -oNmapACKScan.txt 117.X.X.X

# UDP scan
nmap -sU TARGET

# packet tracing
--packet-trace

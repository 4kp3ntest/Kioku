# Normal scan: ping sweep, TCP scan
# Agnostic scan: -Pn

# Ping sweep
nmap -sP 192.168.1.1/24

# Check most used ports and try to determine Service running on open port
nmap -sV 192.168.1.100

## TESTOUT
nmap -v -sS -A -T4 target

# UDP scan
nmap -sU TARGET

# packet tracing
--packet-trace

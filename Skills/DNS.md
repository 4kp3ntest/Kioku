# RFC 1034

arch : bind
debian : bind9


## Tutorial @ https://blog.mansshardt.net/bind9-dns-server-einrichten-unter-debian/
### DNS Server einrichten
1. Locale zone for following setup in db.intra.domain.com
    Web und Mail-Server (192.168.1.1)
    Primärer DNS Server (192.168.1.2)
    Sekundärer DNS Server (192.168.1.3)
2. Add it to /etc/bind/named.conf.local
3. Check
4. Reverse Lookup Zone db.192.168.1
5. Erneut einbinden
6. Check again
### Second DNS Server genauso
### Security
1. generate key pair for Zone transfers 
2. Add keys to configuration
3. Update Zone configuration
4. Deny all requestst (for zone transfer) except authorized ones
5. Define ACL for clients


## Misc
/etc/bind/named.conf.local
/etc/bind/named.conf.options

- Availability of data is important
- Zonendatai speichert Satz von Resource Records
- for each Zone there is an autoritativer Nameserver that is considered trusted

###[ DNS ]### 
    id        = 55491
    qr        = 0
    opcode    = QUERY
    aa        = 0
    tc        = 0
    rd        = 1
    ra        = 0
    z         = 0
    ad        = 0
    cd        = 0
    rcode     = ok
    qdcount   = 1
    ancount   = 0
    nscount   = 0
    arcount   = 0
    \qd        \
     |###[ DNS Question Record ]### 
     |  qname     = 'google.de.'
     |  qtype     = AAAA
     |  qclass    = IN
    \an
     |###[ DNS Resource Record ]### 
        |  rrname    = '131.16.217.172.in-addr.arpa.'
        |  type      = PTR
        |  rclass    = IN
        |  ttl       = 17167
        |  rdlen     = 28
        |  rdata     = 'zrh04s06-in-f131.1e100.net.'
    ns        = None
    ar        = None


## qtypes
SOA RR:     Parameter der Zone, wie z. B. Gültigkeitsdauer oder Seriennummer, festgelegt.
NS RR:      Verknüpfungen (Delegierungen) der Server untereinander realisiert.
A RR:       name to IPv4-addr
AAAA RR:    name to IPv6-addr
CNAME RR:   points from one name to another
MX RR:      references name to MAILSERVER -> SMTP #special
PTR RR:     references IP addr to name (Reverse Lookup) IPv4 & IPv6! 
TXT RR:     kann einem Namen einen frei definierbaren Text zuweisen (Spamabwehr)

[definition in nsswitch.conf in hosts table]

file: reads /etc/hosts
dns: reads /etc/resolv.conf

## Glossary
SOA : Start of Authority
ACL : Access Control List

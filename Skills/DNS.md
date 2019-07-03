# RFC 1034

SOA : Start of Authority

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

nss-resolve(8)
nss-myhostname(8)
nss-mymachines(8)

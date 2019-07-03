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
SOA RR: Parameter der Zone, wie z. B. Gültigkeitsdauer oder Seriennummer, festgelegt.
NS RR: Verknüpfungen (Delegierungen) der Server untereinander realisiert.
(Mit folgenden Record-Typen werden die eigentlichen Daten definiert:)
A RR: name to IPv4-addr
AAAA RR: name to IPv6-addr
CNAME RR: verweist von einem Namen auf einen anderen Namen.
MX RR: weist einem Namen einen Mailserver zu. Er stellt eine Besonderheit dar, da er sich auf einen speziellen Dienst im Internet, nämlich die E-Mailzustellung mittels SMTP, bezieht. Alle anderen Dienste nutzen CNAME, A und AAAA Resource Records für die Namensauflösung.
PTR RR: weist einer IP-Adresse einen Namen zu (Reverse Lookup) und wird für IPv4 und IPv6 gleichermaßen benutzt, nur für IPv4 unterhalb der Domain „IN-ADDR.ARPA.“ und für IPv6 unterhalb von „IP6.ARPA.“.
TXT RR: kann einem Namen einen frei definierbaren Text zuweisen (Spamabwehr)

[definition in nsswitch.conf in hosts table]

file: reads /etc/hosts
dns: reads /etc/resolv.conf

nss-resolve(8)
nss-myhostname(8)
nss-mymachines(8)

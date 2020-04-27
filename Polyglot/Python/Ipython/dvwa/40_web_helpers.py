def bs4_prettify_raw(content):
    modulename = 'BeautifulSoup'
    if modulename in globals():
        soup = BeautifulSoup(content, 'html.parser')
        print(soup.prettify())
    else:
        print('from bs4 import BeautifulSoup')

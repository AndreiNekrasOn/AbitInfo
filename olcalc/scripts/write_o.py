import requests

url = "http://rsr-olymp.ru"
page_code = requests.get(url)
f = open('olymps_to_parse.html', 'wb')
a = page_code.content
f.write(a)
f.close()
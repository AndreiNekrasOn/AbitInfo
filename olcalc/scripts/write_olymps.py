import requests

url = "http://rsr-olymp.ru"
page_code = requests.get(url)
f = open('olymps_to_parse.html', 'w')
a = (str(page_code.content.decode('utf-8')))
f.write(a)
f.close()



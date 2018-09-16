import requests

url = "http://rsr-olymp.ru"
page_code = requests.get(url)
f = open('olymps_to_parse.txt', 'w')
a = (str(page_code.content))
f.write(a)
f.close()



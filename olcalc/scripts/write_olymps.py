# from
import requests
from bs4 import BeautifulSoup

url = "http://rsr-olymp.ru"
page_code = requests.get(url)
soup = BeautifulSoup(page_code.content, 'html.parser')

f = open('olymps_to_parse.html', 'w')
f.write(str(soup))
f.close()



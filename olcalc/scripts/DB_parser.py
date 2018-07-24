import requests
from bs4 import BeautifulSoup

url = "http://vuzoteka.ru/%D0%B2%D1%83%D0%B7%D1%8B/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0?"
page_code = requests.get(url)
soup = BeautifulSoup(page_code.content, 'html.parser')
print(a)

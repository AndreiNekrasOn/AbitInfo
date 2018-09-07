import requests
from bs4 import BeautifulSoup

url_base = "https://propostuplenie.ru/university/vuzy-moskvy/"
f = open('uni.html', 'w', encoding='utf-8')
for page_number in range(1, 19):
    payload = {'Region[]': 15, 'UniverPager': page_number}
    page_code = requests.get(url_base, params=payload)
    a = (str(page_code.content.decode('utf-8')))
    f.write(a)
f.close()


import requests
from bs4 import BeautifulSoup

def get_tagInput_value(url):
    page_code = requests.get(url)
    soup = BeautifulSoup(page_code.content, 'html.parser')
    return [tag['name'] for tag in soup.select('input[type|=text]')]


url_sites = "https://www.crummy.com/software/BeautifulSoup/bs4/doc/genindex.html"
Input_names = get_tagInput_value(url_sites)

d={}
for i in range(0, len(Input_names)):
    d[Input_names[i]] = "lalala"
r = requests.post(url_sites, data=d)
print(r)



print(Input_names)

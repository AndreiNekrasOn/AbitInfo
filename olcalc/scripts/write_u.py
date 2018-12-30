import requests
from bs4 import BeautifulSoup
url_base = "https://propostuplenie.ru/university/vuzy-moskvy/"
f = open('uni.txt', 'w+')
for page_number in range(1, 19):
    payload = {'Region[]': 15, 'UniverPager': page_number}
    page_code = requests.get(url_base, params=payload)
    soup = BeautifulSoup(page_code.content.decode('utf-8'), 'html.parser')
    Univer_div = soup.find('div', {'class': 'col-xs-9 ajax-content unwrapped'})
    Univer_links = Univer_div.find_all('a', {'class': 'title'})
    for link in Univer_links:
        url_univer = "https://propostuplenie.ru" + link.get('href')  # + "/#tab-2"
        page_code = requests.get(url_univer)
        soup = BeautifulSoup(page_code.content.decode('utf-8'), 'html.parser')
        try:
            univer_name = str(soup.find('span', {'itemprop': 'name'}).get_text()).strip()
        except AttributeError:
            print('fuck')
        spec_block = soup.find_all('div', {'class': 'block-spec'})
        for spec in spec_block:
            spec_name = str(spec.find('a', {'class': 'block-spec__header'}).get_text()).strip()
            try:
                scoring = int(spec.find('span', {'class': 'scoring'}).get_text()[0:3])
            except AttributeError:
                scoring = 0
            except ValueError:
                scoring = 0

            # Univer_plus.objects.create(title=univer_name, s_title=spec_name, passing_score=scoring)
            a = str([univer_name, spec_name, scoring]) + '\n'
            f.write(a)
f.close()

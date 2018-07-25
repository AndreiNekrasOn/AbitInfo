# from olcalc.models import testOlymp
import requests
from bs4 import BeautifulSoup

url = "http://rsr-olymp.ru/"
# subjects =['литература', 'обществознание', 'история', 'информатика', 'обществознание', 'экономика', 'нанотехнологии',
#            'филология', 'медицина', 'химия', 'математика', 'физика', 'биология', 'право', 'география', 'английский язык',
#            'астрономия', 'естественные науки',]

page_code = requests.get(url)
soup = BeautifulSoup(page_code.content, 'html.parser')
table = soup.find_all('table')[1]
tds = table.find_all('td')[5:]
test_Name = ''
test_Profile = ''
test_Subject = ''
test_Level = ''

first_time_tr = True
counter = 0

for td in tds:
    if td.has_attr:
        first_time_tr = False
    else:
        if td.find('a'):
            counter = 0
            test_Name += td.get_text() + ' '  # maybe iterate next trs rowspan value times
        test_Profile += td.get_text() + ' '  # need to change modes, e.g. : mode 1 -> get_text in Profile, etc..
        test_Subject += td.get_text() + ' '

print(counter)
# trs = soup.find_all("tr")
# for tr in trs:
#     td =
#     print('\n')

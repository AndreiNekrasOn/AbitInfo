#from olcalc.models import TestOlymp
import requests
from bs4 import BeautifulSoup

url = "http://rsr-olymp.ru/"
page_code = requests.get(url)
soup = BeautifulSoup(page_code.content, 'html.parser')

table = soup.find_all('table')[1]
tds = table.find_all('td')[5:]
test_Name = []
test_Profile = []
test_Level = []

except_number = True
mode = 0
row_value = 0

for td in tds:
    if td.has_attr and except_number is True:
        except_number = False
    else:
        if row_value > 0:
            if mode == 0:
                if dub_Name == test_Name[-1]:
                    test_Name.append(td.get_text())
                    dub_Name = test_Name[- 1]
                test_Profile.append(td.get_text())
                mode += 1
            elif mode == 1:
                mode += 1
            else:
                test_Level.append(td.get_text())
                row_value -= 1
                mode = 0
                if row_value == 0:
                    except_number = True

        else:
            test_Name.append(td.get_text())
            dub_Name = test_Name[-1]
            if td.get('rowspan'):
                row_value = int(td.get('rowspan'))
            else:
                row_value = 1

for i in range (0, len(test_Name)):
    print(f'{test_Name[i]}  {test_Profile[i]} {test_Level[i]}')
    #TestOlymp.objects.create(title=test_Name[i], profile=test_Profile[i], level=test_Level[i])
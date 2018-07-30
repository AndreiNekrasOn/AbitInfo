# from olcalc.models import testOlymp
import requests
from bs4 import BeautifulSoup

subjects = ["Русский язык", "Математика", "Физика", "Химия", "История", "Обществознание", "Информатика",
            "Биология", "География", "Иностранный язык", "Русский язык", "Литература"]

url = "http://rsr-olymp.ru/"
page_code = requests.get(url)
soup = BeautifulSoup(page_code.content, 'html.parser')

table = soup.find_all('table')[1]
tds = table.find_all('td')[5:]
test_Name = ''
test_Profile = ''
test_Level = ''

except_number = True
mode = 0
row_value = 0

for td in tds:
    if td.has_attr and except_number is True:
        except_number = False
    else:
        if row_value > 0:
            if mode == 0:
                test_Profile += td.get_text() + '\n'
                mode += 1
            elif mode == 1:
                mode += 1
            else:
                test_Level += td.get_text() + '\n'
                row_value -= 1
                mode = 0
                if row_value == 0:
                    except_number = True

        else:
            test_Name += td.get_text() + '\n'
            if td.get('rowspan'):
                row_value = int(td.get('rowspan'))
            else:
                row_value = 1

print(test_Name)
print('\n\n\n')
print(test_Profile)
print('\n\n\n')
print(test_Level)
from olcalc.models import Olymp
from bs4 import BeautifulSoup


def run():
    page_code = open('olymps_to_parse.html', 'rb')
    soup = BeautifulSoup(page_code, 'html.parser')
    table = soup.find('table', class_='mainTableInfo')
    tds = table.find_all('td')
    test_Name = []
    test_Profile = []
    test_Level = []

    except_number = True
    mode = 0
    row_value = 0
    counter = 0

    for td in tds:
        if counter < 5:
            counter += 1
            continue
        if td.has_attr and except_number is True:
            except_number = False
        else:
            if row_value > 0:
                if mode == 0:
                    if dub_Name == test_Name[-1] and row_value != 1:
                        test_Name.append(dub_Name)
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
        Olymp.objects.create(title=test_Name[i], subject=test_Profile[i], level=test_Level[i])

    page_code.close()
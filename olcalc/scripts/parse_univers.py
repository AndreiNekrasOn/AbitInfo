# from olcalc.models import Univer_plus


def run():
    page_code = open('uni.txt', encoding='utf-8')
    for line in page_code.readlines():
        for chr in line:
            if chr == '[' or chr == "'" or chr == ',':
                chr = ''




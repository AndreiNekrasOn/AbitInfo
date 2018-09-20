from olcalc.models import Univer_plus


def run():
    page_code = open('uni.txt', encoding='utf-8')
    for line in page_code.readlines():
        univer_name = ''
        univer_spec = ''
        univer_ege = ''
        mode = 0
        for chr in line:
            if mode == 0:
                if chr == ',':
                    mode = 1
                    continue
                univer_name += chr
            if mode == 1:
                if '0' <= chr <= '9':
                    mode = 2
                    continue
                if chr == ']':
                    univer_ege = 0
                    continue
                univer_spec += chr
            if mode == 2:
                if chr == ']':
                    mode = 0
                    continue
                univer_ege += chr

        if univer_ege == '':
            univer_ege = 0
        try:
            Univer_plus.objects.create(title=univer_name, s_title=univer_spec, passing_score=univer_ege)
        except ValueError:  # if fucks than fucks, i'm not smart
            continue
    page_code.close()
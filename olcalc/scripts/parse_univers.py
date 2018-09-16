# from olcalc.models import Univer_plus


def run():
    page_code = open('uni.txt', encoding='utf-8')
    for line in page_code.readlines():
        # Univer_plus.objects.create(title=line[0], s_title=line[1], passing_score=line[2])
        cnt = 0
        title = ''
        s_title = ''
        passing_scor = ''
        for chr in line:
            if cnt == 0:
                if chr == "'" or chr == "[":
                    continue
                else:
                    if chr != "'":
                        title += chr
                    else:
                        cnt = 1
            if cnt == 1:
                if chr == "'" or chr == "[":
                    continue
                else:
                    if chr != "'":
                        title += chr
                    else:
                        cnt = 1



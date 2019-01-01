import csv
from olcalc.models import QOlymp


def run():
    with open("olymps_info.csv", "r", encoding="windows-1251") as file:
        reader = csv.DictReader(file, delimiter=",")
        prev_line = ""
        for line in reader:
            if line["Название"]:
                prev_line = line["Название"]

            o = QOlymp(title=prev_line, subject=line["Профиль"], level=line["Уровень"])
            o.save()

from olcalc.models import Olymp, UniverPlus, Subject, TestOlymp


def run():
    Olymp.objects.all().delete()
    UniverPlus.objects.all().delete()
    Subject.objects.all().delete()
    TestOlymp.objects.all().delete()


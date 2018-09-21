from olcalc.models import Olymp, Univer_plus, Subject


def run():
    Olymp.objects.all().delete()
    Univer_plus.objects.all().delete()
    Subject.objects.all().delete()

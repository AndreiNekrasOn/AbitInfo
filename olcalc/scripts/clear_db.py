from olcalc.models import Olymp, UniverPlus, Subject, TestOlymp


def run():
    olymps = Olymp.objects.all()
    olymps.delete()
    univers = UniverPlus.objects.all()
    univers.delete()
    subjects = Subject.objects.all()
    subjects.delete()
    test = TestOlymp.objects.all()
    test.delete()

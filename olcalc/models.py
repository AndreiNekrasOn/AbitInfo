from django.db import models

# Create your models here


class QUniversuty(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class QFaculty(models.Model):  # fuckulty
    title = models.CharField(max_length=200)
    university = models.ForeignKey(QUniversuty, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title) + ' ' + str(self.university.title)


class QSpeciality(models.Model):  # fuckulty
    title = models.CharField(max_length=200)
    faculty = models.ForeignKey(QFaculty, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title) + ' ' + str(self.faculty.title) + ' ' + str(self.faculty.university.title)


class QOlymp(models.Model):
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=200, default="")
    level = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.title) + ' по предмету' + str(self.subject)


class QPrivilege(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class QMapping(models.Model):
    unifac = models.ForeignKey(QSpeciality, on_delete=models.CASCADE)
    olymp = models.ForeignKey(QOlymp, on_delete=models.CASCADE)
    privilege = models.ForeignKey(QPrivilege, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.unifac.title) + ' ' + str(self.unifac.faculty.title) + ' ' + \
               str(self.unifac.faculty.university.title) + ' ' + str(self.olymp.title) + ' ' + str(self.privilege.title)


class Univer_plus(models.Model):
    title = models.CharField(max_length=200)
    # f_title = models.CharField(max_length=200)
    s_title = models.CharField(max_length=200, null=True, )
    # exams = models.ManyToManyField('Subject')
    passing_score = models.PositiveSmallIntegerField()
    olymps = models.ManyToManyField('Olymp', blank=True)
    rating = models.PositiveSmallIntegerField(default=10000)
    privilege = models.CharField(max_length=200, default="Нет")
    # army_cafedra = models.BooleanField()

    def __str__(self):
        return self.title


class Subject(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Olymp(models.Model):
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    level = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.title


class TestFaculty(models.Model):
    title = models.CharField(max_length=200)
    olymps = models.ManyToManyField('Olymp', blank=True)

    def __str__(self):
        return self.title


class TestUniver(models.Model):
    title = models.CharField(max_length=200)
    f_title = models.OneToOneField(TestFaculty, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
#########

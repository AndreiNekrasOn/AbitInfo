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
    subject = models.CharField(max_length=200)
    level = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.title + ' по предмету ' + self.subject


class QPrivilege(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class QPlace(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class QMapping(models.Model):
    unifac = models.ForeignKey(QSpeciality, on_delete=models.CASCADE)
    olymp = models.ForeignKey(QOlymp, on_delete=models.CASCADE)
    privilege = models.ForeignKey(QPrivilege, on_delete=models.CASCADE)
    place = models.ForeignKey(QPlace, on_delete=models.CASCADE, default="")

    def __str__(self):
        return self.unifac.title + ' ' + self.unifac.faculty.title + ' ' + self.unifac.faculty.university.title + ' ' \
               + self.olymp.title + ' ' + self.privilege.title + ' ' + self.place.title

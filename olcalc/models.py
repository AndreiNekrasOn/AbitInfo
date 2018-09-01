from django.db import models

# Create your models here


class Univer_plus(models.Model):
    title = models.CharField(max_length=200)
    # f_title = models.CharField(max_length=200)
    s_title = models.CharField(max_length=200, null=True, )
    # exams = models.ManyToManyField('Subject')
    passing_score = models.PositiveSmallIntegerField()
    olymps = models.ManyToManyField('Olymp', blank=True)
    rating = models.PositiveSmallIntegerField()
    privilege = models.CharField(max_length=200, null=True, )
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

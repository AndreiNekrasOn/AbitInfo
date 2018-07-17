from django.db import models

# Create your models here
class University(models.Model):
    title= models.CharField(max_length = 200)
    faculties= models.ManyToManyField('Faculty')
    rating = models.PositiveSmallIntegerField()
    army_cafedra= models.BooleanField()
    def __str__(self):
        return self.title
    
class Subject(models.Model):
    title= models.CharField(max_length = 200)
    def __str__(self):
        return self.title

class Olymp(models.Model):
    title= models.CharField(max_length = 200)
    subject= models.ManyToManyField('Subject')
    level= models.PositiveSmallIntegerField()
    def __str__(self):
        return self.title
    
class Speciality(models.Model):
    title= models.CharField(max_length = 200)
    def __str__(self):
        return self.title
    
class Faculty(models.Model):
    title= models.CharField(max_length = 200)
    passing_score= models.PositiveSmallIntegerField()
    olymps= models.ManyToManyField('Olymp')
    specialities= models.ManyToManyField('Speciality')
    def __str__(self):
        return self.title

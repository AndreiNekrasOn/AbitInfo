from django.db import models

# Create your models here
class University(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    faculties= models.ManyToManyField('Faculty')
    title= models.CharField(max_length = 200)
    army_cafedra= models.BooleanField()
    rating = models.PositiveSmallIntegerField()
    def __str__(self):
        return self.title
    
class Subject(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title= models.CharField(max_length = 200)
    def __str__(self):
        return self.title

class Olymp(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title= models.CharField(max_length = 200)
    subject= models.ForeignKey('Subject', on_delete=models.CASCADE)
    level= models.PositiveSmallIntegerField()
    def __str__(self):
        return self.title
    
class Speciality(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title= models.CharField(max_length = 200)
    def __str__(self):
        return self.title
    
class Faculty(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title= models.CharField(max_length = 200)
    passing_score= models.PositiveSmallIntegerField()
    olymps= models.ForeignKey('Olymp', on_delete=models.CASCADE)
    specialities= models.ForeignKey('Speciality', on_delete=models.CASCADE)
    def __str__(self):
        return self.title

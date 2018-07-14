from django.db import models

# Create your models here
        
class Olymp(models.Model):
    name: models.CharField(max_length = 100)
    subject: models.CharField(max_length = 20)
    level: models.AutoField()
    def __str__(self):
        return self.title
    
class Speciality(models.Model):
    name: models.CharField(max_length = 20)
    def __str__(self):
        return self.title
    
class Faculty(models.Model):
    name: models.CharField(max_length = 20)
    passing_score: models.AutoField()
    olymps: models.ForeignKey('Olymp', on_delete=models.SET_NULL)
    specialities: models.ForeignKey('Speciality', on_delete=models.SET_NULL)
    def __str__(self):
        return self.title

class University(models.Model):
    faculties: models.ManyToManyField('Faculty')
    name: models.CharField(max_length = 100)
    army_cafedra: models.BooleanField()
    rating: models.AutoField()
    def __str__(self):
        return self.title
    

        



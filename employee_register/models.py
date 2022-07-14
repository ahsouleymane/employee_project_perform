from django.db import models

# Create your models here.
class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Niveau(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    mobile = models.CharField(max_length=15)
    position = models.ForeignKey(Position,on_delete=models.CASCADE)

class Etudiant(models.Model):
    fullname = models.CharField(max_length=100)
    etu_code = models.CharField(max_length=3)
    mobile = models.CharField(max_length=15)
    niveau = models.ForeignKey(Niveau,on_delete=models.CASCADE)

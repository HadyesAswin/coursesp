from django.db import models

class registration(models.Model):
    name=models.CharField(max_length=25)
    gmail=models.EmailField(max_length=25)
    phoneno = models.IntegerField()
    course=models.CharField(max_length=25)
    Qualification=models.CharField(max_length=25)
    address = models.CharField(max_length=25)
    def __str__(self):
        return self.name

class payment(models.Model):
    name=models.CharField(max_length=25)
    gmail=models.EmailField(max_length=25)
    phoneno = models.IntegerField()
    course=models.CharField(max_length=25)
    Qualification=models.CharField(max_length=25)
    address = models.CharField(max_length=25)
    payments=models.CharField(max_length=25)
    def __str__(self):
        return self.name

# Create your models here.

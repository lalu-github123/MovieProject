from django.db import models

# Create your models here.
class film(models.Model):
    name=models.CharField(max_length=250)
    year=models.IntegerField()
    desc=models.TextField()
    img=models.ImageField()

    def __str__(self):
        return self.name

class film1(models.Model):
    name=models.CharField(max_length=250)
    year=models.IntegerField()
    desc=models.TextField()
    img=models.ImageField()

    def __str__(self):
        return self.name


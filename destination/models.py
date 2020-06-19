from django.db import models

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pic')
    point1 = models.CharField(max_length=100)
    point2 = models.CharField(max_length=100)
    point3 = models.CharField(max_length=100)
    point4 = models.CharField(max_length=100)
    point5 = models.CharField(max_length=100)
    price = models.IntegerField()
    offer = models.BooleanField()

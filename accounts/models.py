from django.db import models

# Create your models here.
class Popular(models.Model):
        name = models.CharField(max_length=100)
        img = models.ImageField()
        desc = models.CharField(max_length=100)
        desc1 = models.CharField(max_length=100)
        desc2 = models.CharField(max_length=100)
        desc3 = models.CharField(max_length=100)
        desc4 = models.CharField(max_length=100)
        desc5 = models.CharField(max_length=100)
        price = models.IntegerField()
        offer = models.BooleanField()
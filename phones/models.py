from django.db import models

# Create your models here.
class Phone(models.Model):
    brand = models.CharField(max_length=30)
    price = models.FloatField()
    release = models.DateField()
    cpu = models.CharField(max_length=25)

    def __str__(self):
        return Phone.brand

from django.db import models


# Create your models here.

class Destination(models.Model):

   
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    desc=models.CharField(max_length=200)
    price=models.CharField(max_length=10)
    offer=models.BooleanField(default=False)

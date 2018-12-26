from django.db import models

# Create your models here.

class DriverInfo(models.Model):
    name=models.CharField(max_length=32)
    email=models.EmailField()
    iphone=models.IntegerField(max_length=11)
    memo=models.TextField()

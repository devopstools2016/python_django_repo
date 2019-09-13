from django.db import models

class EmpData(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile = models.BigIntegerField()
    location = models.CharField(max_length=100)
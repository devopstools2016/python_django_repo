from django.db import models

class EmpData(models.Model):
    ename = models.CharField(max_length=100)
    sal = models.IntegerField()
    mobile = models.BigIntegerField()
    email = models.EmailField(max_length=100)
    location = models.CharField(max_length=100)
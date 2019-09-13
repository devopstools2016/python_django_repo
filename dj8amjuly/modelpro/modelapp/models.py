from django.db import models

class Emp(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=100)
    salary = models.IntegerField()
    email = models.EmailField(max_length=100)
    def __str__(self):
        return self.ename

from django.db import models

class Student(models.Model):
    sname = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    marks = models.IntegerField()

class StudentProxy(Student):
    class Meta:
        proxy = True
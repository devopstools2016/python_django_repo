from django.db import models

class Customer(models.Model):
    cname = models.CharField(max_length=100)
    salesamt = models.IntegerField()

class Emp(Customer):
    ename = models.CharField(max_length=100)
    salary = models.IntegerField()

class Student(Emp):
    sname = models.CharField(max_length=100)
    marks = models.IntegerField()
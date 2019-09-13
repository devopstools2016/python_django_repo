from django.db import models

class Customer(models.Model):
    cid = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=100)
    salesamt = models.IntegerField()

class Emp(models.Model):
    eid = models.AutoField(primary_key=True)
    ename = models.CharField(max_length=100)
    salary = models.IntegerField()

class Skills(models.Model):
    skid = models.AutoField(primary_key=True)
    skname = models.CharField(max_length=100)
    cost = models.IntegerField()

class Student(Customer,Emp,Skills):
    sname = models.CharField(max_length=100)
    marks = models.IntegerField()








class Emp(models.Model):
    id = models.AutoField(primary_key=True)
    ename = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    django = models.Manager()













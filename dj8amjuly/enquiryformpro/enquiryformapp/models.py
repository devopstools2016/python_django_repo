from django.db import models
from multiselectfield import MultiSelectField

class EnquiryData(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.BigIntegerField()
    email = models.EmailField(max_length=100)
    location = models.CharField(max_length=100)

    COUESES_CHOICES = (
        ('py','Python'),
        ('dj','Django'),
        ('java','Java'),
        ('ui','UI'),
        ('Fl','Flask')
    )
    courses = MultiSelectField(max_length=200,choices=COUESES_CHOICES)

    BRANCHES_CHOICES = (
        ('hyd','Hyderabad'),
        ('bang','Bangalore'),
        ('che','Chennai'),
        ('pune','Pune')
    )
    branches = MultiSelectField(max_length=200, choices=BRANCHES_CHOICES)

    SHIFTS_CHOICES = (
        ('mrg','Morning Shift'),
        ('aftn','Afternoon Shift'),
        ('evng','Evening Shift'),
        ('ngt','Night Shift')
    )
    shifts = MultiSelectField(max_length=200, choices=SHIFTS_CHOICES)

    gender = models.CharField(max_length=20)

    start_date = models.DateField(max_length=100)
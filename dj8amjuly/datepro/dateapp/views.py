from django.shortcuts import render
from django.http.response import HttpResponse

import datetime as dt

date1 = dt.datetime.now()

def dateview(request):
    return HttpResponse("<h1>The Current Date and Time is {}</h1>".format(date1))

from django.shortcuts import render
from django.http.response import HttpResponse
def home(request):
    a = "Welcome to Durgasoft"
    return HttpResponse(a)

def contact(request):
    b = "My Contact Number is 999999999"
    return HttpResponse(b)

def services(request):
    c = "We provide all services"
    return HttpResponse(c)

def feedback(request):
    d = "We have good feedback"
    return HttpResponse(d)

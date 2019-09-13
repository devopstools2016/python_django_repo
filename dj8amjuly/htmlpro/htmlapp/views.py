from django.shortcuts import render
from .models import CustData

def cust_view(request):
    if request.method == "POST":
        cname1 = request.POST.get('cname')
        num1 = request.POST.get('num')
        mobile1 = request.POST.get('mobile')
        email1 = request.POST.get('email')

        data = CustData(
            cname=cname1,
            sales=num1,
            mobile=mobile1,
            email=email1
        )
        data.save()
        return render(request,'cust.html')
    else:
        return render(request,'cust.html')

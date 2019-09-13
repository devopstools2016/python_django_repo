from django.shortcuts import render
from .models import ProductData
from .forms import InsertDataForm,UpdateDataForm,DeleteDataForm
from django.http.response import HttpResponse

def main_page(request):
    return render(request,'main_page.html')

def insert_data_view(request):
    if request.method =="POST":
        iform = InsertDataForm(request.POST)
        if iform.is_valid():
            product_id = request.POST.get('product_id')
            product_name = request.POST.get('product_name')
            product_color = request.POST.get('product_color')
            product_class = request.POST.get('product_class')
            product_cost = request.POST.get('product_cost')
            number_of_items = request.POST.get('number_of_items')
            customer_name = request.POST.get('customer_name')
            customer_mobile = request.POST.get('customer_mobile')
            customer_email = request.POST.get('customer_email')

            data = ProductData(
                product_id=product_id,
                product_name=product_name,
                product_color=product_color,
                product_class=product_class,
                product_cost=product_cost,
                number_of_items=number_of_items,
                customer_name=customer_name,
                customer_mobile=customer_mobile,
                customer_email=customer_email
            )
            data.save()
            iform = InsertDataForm()
            return render(request,'insert.html',{'iform':iform})
        else:
            return HttpResponse("User Invalid Data")
    else:
        iform = InsertDataForm()
        return render(request,'insert.html',{'iform':iform})

def retrieve_data_view(request):
    products = ProductData.objects.all()
    return render(request,'fetch.html',{'products':products})


def update_data_view(request):
    if request.method == "POST":
        uform = UpdateDataForm(request.POST)
        if uform.is_valid():
            product_id = request.POST.get('product_id')
            product_cost = request.POST.get('product_cost')

            pid = ProductData.objects.filter(product_id=product_id)

            if pid:
                pid.update(product_cost= product_cost)
                uform = UpdateDataForm()
                return render(request,'update.html',{'uform':uform})
            else:
                return HttpResponse("Invalid Product ID")
        else:
            return HttpResponse('User Invalid Data')
    else:
        uform = UpdateDataForm()
        return render(request,'update.html',{'uform':uform})


def delete_data_view(request):
    if request.method == "POST":
        dform = DeleteDataForm(request.POST)
        if dform.is_valid():
            product_id = request.POST.get('product_id')

            pid = ProductData.objects.filter(product_id=product_id)

            if pid:
                pid.delete()
                dform = DeleteDataForm()
                return render(request,'delete.html',{'dform':dform})
            else:
                return HttpResponse("Invalid Product ID")
        else:
            return HttpResponse('User Invalud Data')
    else:
        dform = DeleteDataForm()
        return render(request,'delete.html',{'dform':dform})
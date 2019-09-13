from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from .models import Hotel

def hotel_image_view(request):
    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)
        if form.is_valid():
            name = request.POST.get('name')
            img = form.cleaned_data.get('hotel_Main_Img')
            data = Hotel(
                name=name,
                hotel_Main_Img=img,
                )
            data.save()
            form = HotelForm()
            return render(request, 'hotel_image_form.html',
                          {'form': form})
    else:
        form = HotelForm()
        return render(request, 'hotel_image_form.html',
                  {'form': form})

def images(request):
    imgs = Hotel.objects.all()
    return render(request,'images_display.html',{'imgs':imgs})
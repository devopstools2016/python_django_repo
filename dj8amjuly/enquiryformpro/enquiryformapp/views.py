from django.shortcuts import render
from .models import EnquiryData
from .forms import EnquiryForm
from django.http.response import HttpResponse

def enquiry_view(request):
    if request.method == "POST":
        eform = EnquiryForm(request.POST)
        if eform.is_valid():
            name = request.POST.get('name')
            mobile = request.POST.get('mobile')
            email = request.POST.get('email')
            location = request.POST.get('location')
            courses = eform.cleaned_data.get('courses')
            branches = eform.cleaned_data.get('branches')
            shifts = eform.cleaned_data.get('shifts')
            gender = eform.cleaned_data.get('gender')
            start_date = eform.cleaned_data.get('start_date')

            data = EnquiryData(
                name=name,
                mobile=mobile,
                email=email,
                location=location,
                courses=courses,
                branches=branches,
                shifts=shifts,
                gender=gender,
                start_date=start_date
            )
            data.save()
            eform = EnquiryForm()
            return render(request,'enquiry.html',{'eform':eform})
        else:
            return HttpResponse("User Invalid Data")
    else:
        eform = EnquiryForm()
        return render(request,'enquiry.html',{'eform':eform})
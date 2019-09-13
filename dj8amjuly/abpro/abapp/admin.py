from django.contrib import admin

from .models import Customer,Emp,Student

class AdminCustomer(admin.ModelAdmin):
    list_display = ['name','location','salesamt']
class AdminEmp(admin.ModelAdmin):
    list_display = ['name','location','salary']
class AdminStudent(admin.ModelAdmin):
    list_display = ['name','location','marks']

admin.site.register(Customer,AdminCustomer)
admin.site.register(Emp,AdminEmp)
admin.site.register(Student,AdminStudent)

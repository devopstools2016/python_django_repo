from django.contrib import admin
from .models import Customer,Emp,Student

class AdminCustomer(admin.ModelAdmin):
    list_display = ['cname','salesamt']
class AdminEmp(admin.ModelAdmin):
    list_display = ['ename','salary']
class AdminStudent(admin.ModelAdmin):
    list_display = ['sname','marks']

admin.site.register(Customer,AdminCustomer)
admin.site.register(Emp,AdminEmp)
admin.site.register(Student,AdminStudent)
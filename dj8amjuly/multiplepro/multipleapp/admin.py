from django.contrib import admin
from .models import Customer,Emp,Skills,Student

class AdminCustomer(admin.ModelAdmin):
    list_display = ['cname','salesamt']
class AdminEmp(admin.ModelAdmin):
    list_display = ['ename','salary']
class AdminSkills(admin.ModelAdmin):
    list_display = ['skname','cost']
class AdminStudent(admin.ModelAdmin):
    list_display = ['sname','marks']

admin.site.register(Customer,AdminCustomer)
admin.site.register(Emp,AdminEmp)
admin.site.register(Skills,AdminSkills)
admin.site.register(Student,AdminStudent)

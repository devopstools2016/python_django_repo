from django.contrib import admin

from .models import Student,StudentProxy

class AdminStudent(admin.ModelAdmin):
    list_display = ['sname','location','email','marks']

class AdminStudentProxy(admin.ModelAdmin):
    list_display = ['sname','location','email','marks']

admin.site.register(Student,AdminStudent)
admin.site.register(StudentProxy,AdminStudentProxy)

from django.contrib import admin

from .models import Student,Course

class AdminStudent(admin.ModelAdmin):
    list_display = ['name','location','email']
class AdminCourse(admin.ModelAdmin):
    list_display = ['cname','cost']

admin.site.register(Student,AdminStudent)
admin.site.register(Course,AdminCourse)
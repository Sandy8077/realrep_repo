from django.contrib import admin
from testaap.models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['rollno','name','dob','marks','email','phone','address']
admin.site.register(Student,StudentAdmin)

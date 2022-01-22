from django.shortcuts import render
from testaap.models import *


# Create your views here.
def home_view(request):
    return render(request,"testaap/home.html")
def record_page(request):
    student_list=Student.objects.all()
    return render(request,'testaap/record.html',{'student_list':student_list})

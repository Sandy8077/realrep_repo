

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','yourself.settings')
import django
django.setup()
from testaap.models import Student



from faker import Faker
from random import *
fake=Faker()






def phoneNo():
    rand=randint(6,9)
    p=str(rand)
    for i in range(9):
        p=p+str(randint(0,9))
    return int(p)

def populate(n):
    for i in range(n):
        froll_no=fake.random_int(min=1,max=999)
        fname=fake.name()
        fdob=fake.date()
        fmarkes=fake.random_int(min=1,max=100)
        femail=fake.email()
        fphone=phoneNo()
        faddress=fake.address()
        Student_record=Student.objects.get_or_create(rollno=froll_no,name=fname,dob=fdob,marks=fmarkes,email=femail,phone=fphone,address=faddress)

populate(60)

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import string
import random
from datetime import datetime , timedelta
from random import randrange
from Abhi.models import Admin,Mobile

def date(start,end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds  
    random_second = randrange(int_delta)
    return start + timedelta(seconds = random_second)

def save(request):
    for i in range(0,10):
        d1 = datetime.strptime('1/1/2019 1:00 PM','%m/%d/%Y %I:%M %p') 
        d1 = datetime.strptime('1/2/2019 4:00 PM','%m/%d/%Y %I:%M %p') 
        d2 = datetime.strptime('1/3/2019 1:00 AM','%m/%d/%Y %I:%M %p') 
        d2 = datetime.strptime('1/4/2019 4:00 AM','%m/%d/%Y %I:%M %p') 
        e1 = date(d1,d2)
        e2 = date(d1,d2)
        letters = string.ascii_uppercase+string.digits
        voucher = ''.join(random.choice(letters) for i in range(10))
        
        a = Admin(voucher = voucher,facevalue = 120 , startdate = e1 ,enddate = e2)
        a.save()
    return HttpResponse ('Post Query')

def get_all(request):
    a = Admin.objects.all()
    s = [{i.facevalue:i.voucher,i.startdate:i.voucher,i.enddate:i.voucher} for i in a]
    return HttpResponse(s)

def dis_vouch(request,mob):
    r = random.randrange(1,11)
    a =Admin.objects.all()
    a = Admin.objects.get(voucher = a[r].voucher)
    print(a.voucher)
    #admi = Admin.objects.get(voucher = a.voucher)
    m = Mobile(admi = Admin(voucher = a.voucher) ,mob = mob )
    m.save()
    
    return HttpResponse('Post Query')

def get_vouch(request):
    m = Mobile.objects.all()
    s1 = [{i.mob:i.admi.voucher} for i in m]
    return HttpResponse(s1)

def marchant_login(request,mob):
    m = Mobile.objects.all()
    print(mob)
    for i in m:
        print(i.mob)
        if(mob == i.mob):
            return HttpResponse('login successfull')
            break
        else:
            return HttpResponse('login failed')
            break

def Read_vouch(request,mob):
    m = Mobile.objects.all()
    l=[]
    l1=[]
    for i in m:
        l.append(i.mob)
        l1.append(i.admi.voucher)
    print(l)
    print(l1)
    m = Mobile.objects.get(mob = mob)
    if m.mob in l:
        if m.admi.voucher in l1:
            return HttpResponse("voucher Redemed")    
        # else:
        #     return HttpResponse("no. has voucher")


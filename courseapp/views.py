from django.shortcuts import render,redirect
from.models import *

def home(request):
    return render(request,'home.html')

def pyhome(request):
    return render(request,'python/pythonhm.html')
def pythonreg(request):
    return render(request,'python/pythonreg.html')

def pythonsdads(request):
    return render(request,'python/pythonsdads.html')

def python_registration(request):
    if request.method=='POST':
        full_name=request.POST['names']
        gmail = request.POST['uemail']
        contact=request.POST['phone']
        courses = request.POST['course']
        quali = request.POST['quali']
        addr=request.POST['address']
        data = registration.objects.create(name=full_name, gmail=gmail, phoneno=contact, course=courses,Qualification=quali, address=addr)
        data.save()
    return render(request,'python/pythonreg.html')


def pythonpay(request):
    return render(request,'python/pythonpay.html')

def flutterhm(request):
    return render(request,'flutter/flutterhm.html')

def flutterreg(request):
    return render(request,'flutter/flutterreg.html')

def flutter_registration(request):
    if request.method=='POST':
        full_name=request.POST['names']
        gmail = request.POST['uemail']
        contact=request.POST['phone']
        courses = request.POST['course']
        quali = request.POST['quali']
        addr=request.POST['address']
        data = registration.objects.create(name=full_name, gmail=gmail, phoneno=contact, course=courses,Qualification=quali, address=addr)
        data.save()
    return render(request, 'flutter/flutterreg.html')


def flutterpay(request):
    return render(request,'flutter/flutterpay.html')

def javahm(request):
    return render(request,'java/javahm.html')

def javareg(request):
    return render(request,'java/javareg.html')

def java_registration(request):
    if request.method=='POST':
        full_name=request.POST['names']
        gmail = request.POST['uemail']
        contact=request.POST['phone']
        courses = request.POST['course']
        quali = request.POST['quali']
        addr=request.POST['address']
        data = registration.objects.create(name=full_name, gmail=gmail, phoneno=contact, course=courses,Qualification=quali, address=addr)
        data.save()
    return render(request, 'java/javareg.html')

def javapay(request):
    return render(request,'java/javapay.html')

def sqlhm(request):
    return render(request,'sql/sqlhm.html')

def sqlreg(request):
    return render(request,'sql/sqlreg.html')

def sql_registration(request):
    if request.method=='POST':
        full_name=request.POST['names']
        gmail = request.POST['uemail']
        contact=request.POST['phone']
        courses = request.POST['course']
        quali = request.POST['quali']
        addr=request.POST['address']
        data = registration.objects.create(name=full_name, gmail=gmail, phoneno=contact, course=courses,Qualification=quali, address=addr)
        data.save()
    return render(request, 'sql/sqlreg.html')


def sqlpay(request):
    return render(request,'sql/sqlpay.html')

def python_pay(request):
    if request.method=='POST':
        full_name=request.POST['names']
        gmail = request.POST['uemail']
        contact=request.POST['phone']
        courses = request.POST['course']
        quali = request.POST['quali']
        addr=request.POST['address']
        pay=request.POST['paymentid']
        data=payment.objects.create(name=full_name,gmail=gmail,phoneno=contact,course=courses,Qualification=quali,address=addr,payments=pay)
        data.save()
    return render(request,'python/pythonpay.html')

def flutter_pay(request):
    if request.method=='POST':
        full_name=request.POST['names']
        gmail = request.POST['uemail']
        contact=request.POST['phone']
        courses = request.POST['course']
        quali = request.POST['quali']
        addr=request.POST['address']
        pay=request.POST['paymentid']
        data = payment.objects.create(name=full_name, gmail=gmail, phoneno=contact, course=courses, Qualification=quali,address=addr, payments=pay)
        data.save()
    return render(request, 'flutter/flutterpay.html')

def java_pay(request):
    if request.method=='POST':
        full_name=request.POST['names']
        gmail = request.POST['uemail']
        contact=request.POST['phone']
        courses = request.POST['course']
        quali = request.POST['quali']
        addr=request.POST['address']
        pay=request.POST['paymentid']
        data = payment.objects.create(name=full_name, gmail=gmail, phoneno=contact, course=courses, Qualification=quali,address=addr, payments=pay)
        data.save()
    return render(request, 'java/javapay.html')

def sql_pay(request):
    if request.method=='POST':
        full_name=request.POST['names']
        gmail = request.POST['uemail']
        contact=request.POST['phone']
        courses = request.POST['course']
        quali = request.POST['quali']
        addr=request.POST['address']
        pay=request.POST['paymentid']
        data = payment.objects.create(name=full_name, gmail=gmail, phoneno=contact, course=courses, Qualification=quali,address=addr, payments=pay)
        data.save()
    return render(request, 'sql/sqlpay.html')

# Create your views here.

def testtt(request):
    return redirect('abcd')
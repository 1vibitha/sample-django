from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import department,Doctor
from . forms import Bookingform
# Create your views here.
def index(request):
    # return HttpResponse("hello welcome")'
    nums=range(0,10)
    person={
        'name':'John',
        'age':30,
        'place':'Thrissur',
        'num':nums,
        'number':[1,2,3,4,5,6,7,8,9,10]
    }
    return render(request,'index.html',person)


def about(request):
    return render(request,'about.html')


def show(request):
    dis={
        'number':[1,2,3,4,5,6,7,8,9,10]
    }
    return render(request,'show.html',dis)


def demo(request):
    return render(request,'demo.html')

def dept(request):
    depts={
        'dep':department.objects.all()
    }
    return render(request,'dept.html',depts)
def doct(request):
    docts={
        'doc':Doctor.objects.all()
    }
    return render(request,'doctor.html',docts)

def booking(request):
    if request.method=='POST':
        form=Bookingform(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'booking.html')
    else:
        form=Bookingform()
    dic_form={
            'form':form
        }
    return render(request,'booking.html',dic_form)



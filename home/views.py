from django.shortcuts import render
from django.http import HttpResponse
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





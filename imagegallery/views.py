from django.shortcuts import render
from . models import ImageGallery
from . forms import Imageform
# Create your views here.
def image(request):
    if request.method=="POST":
        form=Imageform(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
    else:
        form=Imageform()
    img=ImageGallery.objects.all()
    dic_form={
            'form':form,
            'img':img

        }
    return render(request,'imagegallery.html',dic_form)


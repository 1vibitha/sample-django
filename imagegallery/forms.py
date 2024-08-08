from django import forms 
from . models import ImageGallery
class Imageform(forms.ModelForm):
    class Meta:
        model=ImageGallery
        fields=('caption','Image')
from django.shortcuts import render
from .models import MyImages
# Create your views here.


def allmyimages(request):
    images = MyImages.objects.all()
    context = {
        'images':images
    }
    return render(request,'images.html',context)

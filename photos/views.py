from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to my Gallery')

def gallery(request):
    return render(request,'gallery.html')

def viewPhoto(request):
    return render(request,'photo.html')

def locatePhoto(request):
    return render(request,'location.html')

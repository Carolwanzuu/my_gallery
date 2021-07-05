from photos.models import Category, Photo
from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to my Gallery')

def gallery(request):
    categories = Category.objects.all()
    photos = Photo.objects.all()

    context = {'categories':categories,'photos':photos}

    return render(request,'gallery.html',context)

def viewPhoto(request,pk):
     photos = Photo.objects.get(id=pk)
     return render(request,'photo.html',{'photos':photos})

def locatePhoto(request):
    return render(request,'location.html')

def search_image(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Photo.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"articles": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

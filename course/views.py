from django.shortcuts import render
from .models import*
from blog.models import blogCatagory
# Create your views here.
def classPage(request):
    course = courseModel.objects.all()

    context={
        'course':course,
    }
    return render(request, 'class.html', context)
def galleryPage(request):
    gallery = galleryModel.objects.all()
    cat = blogCatagory.objects.all()
    context={
        'gallery':gallery,
        'cat':cat,
    }

    return render(request, 'gallery.html', context)

def bookingPage(request):
    return render(request, 'booking.html')

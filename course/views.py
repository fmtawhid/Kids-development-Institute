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
    course = courseModel.objects.all()
    if request.method == 'POST':
        vname = request.POST['name']
        vemail = request.POST['email']
        vnumber = request.POST['number']
        vcourse = request.POST['course']

        selected_course = courseModel.objects.get(pk=vcourse)

        seat = bookingModel(name = vname, email = vemail, mobile = vnumber, course = selected_course)
        seat.save()

    context = {
        'course':course,
    }
    return render(request, 'booking.html', context)

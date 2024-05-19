from django.shortcuts import render, redirect
from .models import *
from blog.models import *
from course.models import*


# Create your views here.
def homePage(request):
    course = courseModel.objects.all()
    doc = blogModel.objects.all()
    team = teamModel.objects.all()
    review = testimonialModel.objects.all()

    context = {
        'course':course,
        'doc':doc,
        'team':team,
        'review':review,

    }
    return render(request, 'index.html', context)

def aboutPage(request):
    team = teamModel.objects.all()

    context = {
        'team':team,
    }
    return render(request, 'about.html', context)

def contactPage(request):
    if request.method == 'POST':
        vname = request.POST['name']
        vemail = request.POST['email']
        vmessage = request.POST['message']

        cont = contactModel(name=vname, email=vemail, message=vmessage)
        cont.save()
    
    return render(request, 'contact.html',)


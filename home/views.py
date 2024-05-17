from django.shortcuts import render
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
    return render(request, 'about.html')
def contactPage(request):
    return render(request, 'contact.html')

from django.urls import path
from .views import*

urlpatterns = [
    path('', homePage, name='home'),
    path('about/', aboutPage, name='about'),
    path('contact/', contactPage, name='contact'),
]
from django.urls import*
from .views import*
urlpatterns = [
    path('', classPage, name='class'),
    path('gallery', galleryPage, name='gallery'),
    path('booking', bookingPage, name='booking'),
]
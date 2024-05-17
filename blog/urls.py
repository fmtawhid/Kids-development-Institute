from django.urls import*
from .views import*
urlpatterns = [
    path('', blogPage, name='documentary'),
    path('<slug:slug>/', singelPage, name='single')
]
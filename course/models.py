from django.db import models
from blog.models import blogCatagory
# Create your models here.

class courseModel(models.Model):

    title=models.CharField(max_length=30, unique=True)
    image = models.ImageField(upload_to='course')
    description = models.TextField(max_length=200, unique=True)
    ageLimit = models.CharField(max_length=10)
    seat = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.title
    

class testimonialModel(models.Model):
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    image = models.FileField(upload_to='parents')
    saying = models.TextField(max_length=100)

    def __str__(self):
        return self.name

class galleryModel(models.Model):
    title = models.CharField(max_length=200)
    image = models.FileField(upload_to='gallery')
    category = models.ForeignKey(blogCatagory, on_delete = models.CASCADE)

    def __str__(self):
        return self.title
    
class bookingModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.IntegerField()
    course = models.ForeignKey(courseModel, on_delete=models.CASCADE)
    bookingDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class blogCatagory(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField()
    
    def __str__(self):
        return self.title
    
class blogModel(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField()
    image = models.FileField(upload_to='blogImage')
    description = RichTextField()
    category = models.ForeignKey(blogCatagory, on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


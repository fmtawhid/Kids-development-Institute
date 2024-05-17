from django.db import models

# Create your models here.
class teamModel(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    image = models.FileField(upload_to='team')
    twitter = models.URLField()
    youtube = models.URLField()
    linkedin = models.URLField()
    def __str__(self):
        return self.name
    


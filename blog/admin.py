from django.contrib import admin
from .models import*
# Register your models here.
class cat_admin(admin.ModelAdmin):
    prepopulated_fields={'slug':['title']}
class blog_admin(admin.ModelAdmin):
    prepopulated_fields={'slug':['title']}

admin.site.register(blogCatagory, cat_admin)
admin.site.register(blogModel, blog_admin)

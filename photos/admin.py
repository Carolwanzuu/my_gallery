from django.contrib import admin
from .models import Category, Image

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    filter_horizontal=('image')

admin.site.register(Category)
admin.site.register(Image)
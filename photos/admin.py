from django.contrib import admin
from .models import Category, Photo

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    filter_horizontal=('photo')

admin.site.register(Category)
admin.site.register(Photo)
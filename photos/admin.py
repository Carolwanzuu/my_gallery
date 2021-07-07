from django.contrib import admin
from .models import Category, Photos

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    filter_horizontal=('photo')

admin.site.register(Category)
admin.site.register(Photos)
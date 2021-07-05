from django.db import models
from django.db.models.fields.related import OneToOneField

# Create your models here.
class Category(models.Model):
    name= models.CharField(max_length=100, null =False, blank=False)

    def __str__(self):
        return self.name



class Image(models.Model):
    image = models.ImageField(null=False,blank=False)
    image_name = models.CharField(max_length=30)
    image_description= models.TextField(blank=True)
    # location= models.CharField(max_length=100)
    category=models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True )
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.image_name

# class Location(models.Model):
#     name=models.CharField(max_length=50)
#     image=models.ForeignKey(Image,on_delete=models.CASCADE,)


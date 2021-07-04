from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField()
    image_name = models.CharField(max_length=30)
    image_description= models.CharField(max_length=100)
    # location= models.CharField(max_length=100)
    image_category=models.CharField(max_length=50)

# class Location(models.Model):
#     name=models.CharField(max_length=50)
#     image=models.ForeignKey(Image,on_delete=models.CASCADE,)


from django.db import models
# from django.db.models. fields.related import BigAutoField

# Create your models here.
class Category(models.Model):
    name= models.CharField(max_length=100, null =False, blank=False)

    def __str__(self):
        return self.name

# class Location(models.Model):
#     location = models.CharField(max_length=300)



class Photo(models.Model):
    photo = models.ImageField(null=False,blank=False)
    photo_name = models.CharField(max_length=30)
    description= models.TextField(blank=True)
    # location=models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True )
    category=models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True )
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.photo_name

    @classmethod
    def search_by_category(cls,search_term):
        image_search = cls.objects.filter(title__icontains=search_term)
        return image_search


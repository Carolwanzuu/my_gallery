from django.db import models
# from django.db.models. fields.related import BigAutoField

# Create your models here.
class Category(models.Model):
    name= models.CharField(max_length=100, null =False, blank=False)

    def __str__(self):
        return self.name

    @classmethod
    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

class Location(models.Model):
    location = models.CharField(max_length=300)

    def __str__(self):
        return self.location

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()




class Photos(models.Model):
    image = models.ImageField(null=False, blank=False)
    photo_name = models.CharField(max_length=30)
    description= models.TextField(blank=True)
    location=models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True )
    category=models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True )
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.photo_name

    @classmethod
    def get_image_by_id(cls, image_id):
        image = Photos.objects.get(id=image_id)
        return image.url

    @classmethod
    def search_by_category(cls,search_term):
        image_search = cls.objects.filter(title__icontains=search_term)
        return image_search

    @classmethod
    def filter_by_location(cls, location):
        Image_Location = Photos.objects.filter(location_name=location).all()
        return  Image_Location.url

    @classmethod
    def all_images(cls):
        images = cls.objects.all()
        return images 



from django.test import TestCase
from .models import Category, Photo, Location

# Create your tests here.
class TestImage(TestCase):
  def setUp(self):
    self.location = Location(location='Nairobi')
    self.location.saveLocation()

    self.category = Category(category='Food')
    self.category.saveCategory()

    self.image = Photo(image ='photos/test.jpg', image_name = 'test1', image_desc= 'this is a test1', location_id=self.location, category_id=self.category)

  def teardown(self):
    Photo.objects.all().delete()
    Location.objects.all().delete()
    Category.objects.all().delete()

  def test_instance(self):
    self.assertTrue(isinstance(self.image, Photo))

  def test_saveImage(self):
    self.image.save_image()
    images = Photo.objects.all()
    self.assertTrue(len(images)>0)
  
  def test_updateImage(self):
    self.image.save_image()
    self.image.update_image(self.image.id, 'photos/test2.jpg')
    updated_image = Photo.objects.get(id=self.image.id)
    self.assertEqual(updated_image.image, 'photos/test2.jpg')

  def test_deleteImage(self):
    self.image.save_image()
    self.image2 = Photo.objects.create(image ='photos/test3.jpg', image_name = 'test3', image_desc= 'this is a test3', location_id=self.location, category_id=self.category)
    Photo.delete_image(self.image.id)
    self.assertTrue(len(Photo.objects.all())==1)
  
  def test_getImagesById(self):
    self.image.save_image()
    imagefound = Photo.get_images_by_id(self.image.id)
    self.assertEqual(imagefound, self.image)
    
  def test_searchImage(self):
    self.category2 = Category.objects.create(category='Food')
    self.image2 = Photo.objects.create(image ='photos/test3.jpg', image_name = 'test3', image_desc= 'this is a test3', location_id=self.location, category_id=self.category2)
    searchTerm = 'Food'
    self.image.save_image()
    searchResult = Photo.search_image(searchTerm)
    self.assertEqual(searchResult.count(), 2)

  def test_filterlocation(self):
    self.image.save_image()
    self.location2 = Location.objects.create(location='Kisumu')
    self.image2 = Photo.objects.create(image ='photos/test3.jpg', image_name = 'test3', image_desc= 'this is a test3', location_id=self.location2, category_id=self.category)
    filterlocationterm = 'Kisumu'
    searchResult = Photo.filter_by_location(filterlocationterm)
    self.assertEqual(searchResult.count(), 1)

class TestLocation(TestCase):
  def setUp(self):
    self.location = Location(location='Nairobi')

  def test_instance(self):
    self.assertTrue(isinstance(self.location, Location))

  def test_saveLocation(self):
    self.location.saveLocation()
    location = Location.objects.all()
    self.assertTrue(len(location)>0)
  
  def test_deleteLocation(self):
    self.location.saveLocation()
    self.location2 = Location.objects.create(location='USA')
    Location.deleteLocation(self.location2.id)
    self.assertTrue(len(Location.objects.all())==1)

  def test_updateLocation(self):
    update_term = 'USA'
    self.location.saveLocation()
    Location.updateLocation(self.location.id, update_term)  
    updated_one = Location.objects.get(id=self.location.id)
    self.assertEqual(updated_one.location, 'USA')

class TestCategory(TestCase):
  def setUp(self):
    self.category = Category(category='Food')

  def test_instance(self):
    self.assertTrue(isinstance(self.category, Category))

  def test_saveCategory(self):
    self.category.saveCategory()
    category = Category.objects.all()
    self.assertTrue(len(category)>0)

  def test_deleteCategory(self):
    self.category.saveCategory()
    self.category2 = Category.objects.create(category='Travel')
    Category.deleteCategory(self.category2.id)
    self.assertTrue(len(Category.objects.all())==1)


  def test_updateCategory(self):
    update_term = 'Money'
    self.category.saveCategory()
    Category.updateCategory(self.category.id, update_term)  
    updated_one = Category.objects.get(id=self.category.id)
    self.assertEqual(updated_one.category, 'Food')
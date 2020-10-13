from django.test import TestCase

# Create your tests here.
from .models import Image, Category, Location

# Create your tests here.
class ImageTestClass(TestCase):

    def setUp(self):
        self.image = Image(name = 'chelsea', description = 'my favorite soccer club')
        self.image.save_image()

    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))


    def test_save_method(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0) 


    def test_delete_method(self):
        self.new_image = Image(name = 'ford', description = 'my favorite car')  
        self.new_image.save_image() 
        self.new_image.delete_image()
        images = Image.objects.all()
        self.assertEqual(len(images), 1)


    def test_update_method(self):
        self.image = Image(name = 'ferrari', description = 'my second favorite car')
        self.image.save_image()
        self.image = Image(name = 'ferrari', description = 'my second favorite car')        
        self.image.update_image(name = 'ferrari')
        self.image.save_image()
        images = Image.objects.filter(name = 'mustang')
        pics = Image.objects.all()      
        self.assertEqual(len(images), 1)

    def tearDown(self):
        Image.objects.all().delete()

class LocationTestClass(TestCase):
    def setUp(self):
        self.location = Location(name='kenya')
        self.location.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_location(self):
        self.location.save_location()
        locations = Location.get_locations()
        self.assertTrue(len(locations) > 0)

   
    def test_update_location(self):
        new_location = 'england'
        self.location.update_location(self.location.id, new_location)
        changed_location = Location.objects.filter(name='england')
        self.assertTrue(len(changed_location) > 0)

    def test_delete_location(self):
        self.location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)


class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category(name='cars')
        self.category.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_category(self):
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)
    
    def test_update_category(self):
        new_category = 'soccer'
        self.category.update_category(self.category.id, new_category)
        changed_category = Category.objects.filter(name='soccer')
        self.assertTrue(len(changed_category) > 0)   

    def test_delete_category(self):
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)
        

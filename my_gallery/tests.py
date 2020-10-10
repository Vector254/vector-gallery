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
        self.image = Image(name = 'mustang', description = 'my third favorite car')        
        self.image.update_image(name = 'mustang')
        self.image.save_image()
        images = Image.objects.filter(name = 'mustang')
        pics = Image.objects.all()      
        self.assertEqual(len(images), 1)

    def tearDown(self):
        Image.objects.all().delete()
        

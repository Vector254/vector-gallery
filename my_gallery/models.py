from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = '', null = True, blank = True)
    name = models.CharField(max_length=20)	   
    description = models.CharField(max_length=100)	    
    category = models.ForeignKey('Category', on_delete = models.CASCADE, null='True', blank=True)	    
    location = models.ForeignKey('Location', on_delete = models.CASCADE, null='True', blank=True)
    
    def __str__(self):
        return self.name

    def save_image(self):
        self.save()   

    def delete_image(self):
        Image.objects.filter(id = self.pk).delete() 
    
    def update_image(self, **kwargs):
        self.objects.filter(id = self.pk).update(**kwargs) 

    @classmethod
    def get_images(cls):
        images = cls.objects.all()
        return images  

    @classmethod
    def search_by_category(cls, category):
        images = cls.objects.filter(category__name__icontains=category)
        return images 
    
    @classmethod
    def filter_by_location(cls, location):
        image_location = Image.objects.filter(location__name=location).all()
        return image_location

class Category(models.Model):
    name = models.CharField(max_length=15,) 	    


class Location(models.Model):
    name = models.CharField(max_length=20,) 

    @classmethod
    def get_locations(cls):
        locations = Location.objects.all()
        return locations
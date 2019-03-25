from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    profile = models.CharField(max_length =30)
    bio = HTMLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # def save_location(self):
    #     self.save()
    # def delete_location(self):
    #     self.delete()
    
    # def update_location(self, update):
    #     self.location = update
    #     self.save()
    # @classmethod
    # def get_location_id(cls, id):
    #     location = Location.objects.get(pk = id)
    #     return location

    def __str__(self):
        return self.name
class Comments(models.Model):
    comments =HTMLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    # def save_category(self):
    #     self.save()
       

    # def delete_category(self):
    #     self.delete()
    
    # def update_category(self, update):
    #     self.category = update
    #     self.save()

    # @classmethod
    # def get_category_id(cls, id):
    #     category = Category.objects.get(pk = id)
    #     return category

    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to = 'gallery/',blank=False)
    name = models.CharField(max_length =30)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    caption = models.CharField(max_length =60)
    profile= models.ForeignKey(Profile)
    likes = models.CharField(max_length =60)
    comments=models.CharField(max_length =60)
    def save_image(self):
        self.save()
    

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']        

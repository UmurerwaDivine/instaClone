from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    profile = models.ImageField(upload_to = 'gallery/',blank=False)
    bio = HTMLField()
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    follow=models.NullBooleanField(default=False)
    def save_profile(self):
        self.save()

    def update_bio(self):
        self.bio = bio
        self.save()

    def delete_profile(self):
        self.delete()

    def __str__(self):
        return str(self.user)
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
    upload_date = models.DateTimeField(auto_now_add=True,null=True) 

    def save_image(self):
        self.save()
    @classmethod
    def get_images(cls):
        images = cls.objects.all()
        return images

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_caption(self, caption):
        self.caption = caption
        self.save()

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']  
              
class Comment(models.Model):
    comment = models.CharField(max_length=2200)
    image = models.IntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
class Like(models.Model):
    likes = models.IntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
class Follow(models.Model):
     follower=models.ForeignKey(Profile, related_name='follower')
     following=models.ForeignKey(Profile ,related_name='followee')

   

from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField



# Create your models here.

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'profile/', default = 'default.jpg')
    profile_bio = models.CharField(max_length = 100)
    profile_user = models.OneToOneField(User, on_delete = models.CASCADE)
    
    
    def __str__(self):
        return self.profile_bio
    
    
    def save_profile(self):
        self.save()
        
        
    def delete_profile(self):
        self.delete()
        
        
    def update_profile(self):
        Profile.objects.filter(pk = id).update(profile_photo = profile_photo,profile_bio = profile_bio, profile_user = profile_user) 
    
    
    
class Image(models.Model):
    image_path = models.ImageField(upload_to = 'posts/')
    image_name = models.CharField(max_length = 50)
    image_caption = models.TextField(max_length = 300)
    image_profile = models.ForeignKey(User, null = True, on_delete = models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add = True)
    
    
    def __str__(self):
        return self.image_caption
    
    
    def save_image(self):
        self.save()
        
        
    def delete_image(self):
        self.delete()
        
        
    def update_caption(self):
        Image.objects.filter(pk = id).update(image_caption = image_caption)
        
        
        
class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()
    
    
    
class Comment(models.Model):
    comment = models.CharField(max_length = 100)
    image_id = models.ForeignKey(Image)
    profile_id = models.ForeignKey(Profile)
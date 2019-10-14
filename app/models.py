from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'profile/', default = 'default.jpg')
    profile_bio = models.CharField(max_length = 100)
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    
    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance) 
            
    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save() 
        
    def __str__(self):
        return self.user.username
    
    
    def save_profile(self):
        self.save()
        
        
    def delete_profile(self):
        self.delete()
        
        
    def update_profile(self):
        Profile.objects.filter(pk = id).update(profile_photo = profile_photo,profile_bio = profile_bio, user = user) 
        
    @classmethod
    def search_by_username(cls,search_term):
        profile = cls.objects.filter(user__username__icontains = search_term)
    
        return profile
    
    
class Image(models.Model):
    image_path = models.ImageField(upload_to = 'posts/')
    image_name = models.CharField(max_length = 50)
    image_caption = models.TextField(max_length = 300)
    image_author = models.ForeignKey(User, null = True, on_delete = models.CASCADE)
    author_profile = models.ForeignKey(Profile, null = True, on_delete = models.CASCADE, blank=True)

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
    
    
    def __str__(self):
        return self.comment
    
    
    def save_comments(self):
        self.save()


    def delete_comments(self):
        self.delete()
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    # profile_photo = models.ImageField(upload_to = '/profile', default = 'default.jpg')
    profile_bio = models.CharField(max_length = 100)
    profile_user = models.OneToOneField(User, on_delete = models.CASCADE)
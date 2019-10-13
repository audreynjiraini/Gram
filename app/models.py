from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    # profile_photo = models.ImageField(upload_to = '/profile', default = 'default.jpg')
    bio = models.CharField(max_length = 100)
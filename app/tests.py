from django.test import TestCase
from .models import Profile, Image
from django.contrib.auth.models import User


# Create your tests here.

class ProfileTestClass(TestCase):
    
    # Set up method
    def setUp(self):
        self.user = User(username = 'audrey', email = 'audreywncode@gmail.com', password = 'njiraini123')
        self.user.save()
        
        self.audrey = Profile(profile_photo = 'default.jpg', profile_bio = 'Test 1', profile_user = self.user)
        
        
    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.audrey, Profile))
    
    
    # Testing Save Method
    def test_save_profile(self):
        self.audrey.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)
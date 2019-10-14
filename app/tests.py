from django.test import TestCase
from .models import Profile, Image
from django.contrib.auth.models import User


# Create your tests here.

class ProfileTestClass(TestCase):
    
    # Set up method
    def setUp(self):
        self.user = User(username = 'audrey', email = 'audreywncode@gmail.com', password = 'njiraini123')
        self.user.save()
        
        self.audrey = Profile(id = 50, profile_photo = 'default.jpg', profile_bio = 'Test 1', user = self.user)
        
        
    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.audrey, Profile))
    
    
    # Testing Save Method
    def test_save_profile(self):
        self.audrey.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)
        
        
    # Testing delete Method
    def test_delete_profile(self):
        self.audrey.save_profile()
        self.audrey = Profile.objects.get(id = 50)
        
        self.audrey.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)
        
        
    #Testing update method
    def test_update_profile(self):
        self.audrey.save_profile()
        self.audrey = Profile.objects.filter(profile_bio = 'Test 1').update(profile_bio='Test 2')
        
        self.audrey = Profile.objects.get(profile_bio='Test 2')
        self.assertEqual(self.audrey.profile_bio, 'Test 2')
        
        
    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()
        
        
        
class ImageTestClass(TestCase):
    
    # Set up method
    def setUp(self):
        self.audrey = User(username = 'audrey', email = 'audreywncode@gmail.com', password = 'njiraini123')
        self.audrey.save()
        
        self.image = Image(id = 50, image_path = 'image.jpg', image_name = 'Test',image_caption = 'Test 1', image_profile = self.audrey, pub_date = '2019-10-10')
        
        
    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))
    
    
    # Testing Save Method
    def test_save_image(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)
        
        
    # Testing delete Method
    def test_delete_image(self):
        self.image.save_image()
        self.image = Image.objects.get(id = 50)
        
        self.image.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)
        
        
    #Testing update caption method
    def test_update_caption(self):
        self.image.save_image()
        self.image = Image.objects.filter(image_caption = 'Test 1').update(image_caption = 'Test 2')
        
        self.image = Image.objects.get(image_caption = 'Test 2')
        self.assertEqual(self.image.image_caption, 'Test 2')
    
    
    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()
        Image.objects.all().delete()
        
from django import forms
from .models import Profile, Image, Comment


class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label = 'First Name', max_length = 30)
    email = forms.EmailField(label = 'Email')
    
    
class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = []


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['pub_date','image_profile']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['image_id','profile_id']
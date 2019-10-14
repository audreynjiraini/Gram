from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Profile, Image, NewsLetterRecipients
from django.contrib.auth.models import User
from .forms import NewPostsForm, NewProfileForm, NewsLetterForm
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url = '/accounts/login/')
def register(request):
    
    return render(request, 'registration/registration_form.html')



def index(request):
    
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            
            recipient = NewsLetterRecipients(name = name, email = email)
            recipient.save()
            send_welcome_email(name, email)
            
            return HttpResponseRedirect('/accounts/login/')
        
        else:
            form = NewsLetterForm()
            
    return render(request, 'index.html', {'letterForm': form})



@login_required(login_url = '/accounts/login/')
def create_profile(request):
    
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        
        if form.is_valid():
            profile = form.save(commit = False)
            profile.image_profile = current_user
            profile.save()
            
    else:
        form = NewProfileForm()
        
    return render(request, 'create_profile.html', {'form': form})
            
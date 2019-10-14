from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Profile, Image, NewsLetterRecipients
from django.contrib.auth.models import User
from .forms import NewPostsForm, NewProfileForm, NewsLetterForm
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    return render(request, 'index.html')



@login_required(login_url = '/accounts/login/')
def register(request):
    return render(request, 'registration/registration_form.html')
from django.shortcuts import render
from django.views import generic
from .models import Profile


# Create your views here.
class ProfilePage(generic.ListView):
    model = Profile
    template_name = 'account/profile.html'
    context_object_name = 'profiles'
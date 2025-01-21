from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .form import ProfileForm
from .models import Profile
from django.views.generic import CreateView, ListView

# Create your views here.

class CreateProfileView(CreateView):
    model = Profile
    template_name = "profiles/create_profile.html"
    fields = "__all__"
    success_url = "/profiles"

class ProfileView(ListView):
    model = Profile
    template_name = "profiles/view_profile.html"
    context_object_name = "profiles"
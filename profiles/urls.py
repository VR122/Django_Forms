from django.urls import path
from . import views

urlpatterns = [
    path("", views.CreateProfileView.as_view()),
    path("all_profiles", views.ProfileView.as_view())
]
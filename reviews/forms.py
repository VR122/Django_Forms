from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['user_name', 'review', 'rating']
        labels = {
            'user_name': 'Your name',
            'review': 'Your review',
            'rating': 'Your Rating'
        }
        error_messages = {
            'user_name': {
                'required': 'Please enter your name.',
                'max_length': 'Please enter a shorter name.'
            }
        }
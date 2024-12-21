from django import forms

class ReviewForm(forms.Form):
    user_name = forms.CharField(label='Your name',max_length=100, error_messages={
        'required': 'Please enter your name.',
        'max_length': 'Please enter a shorter name.'
    })
    review = forms.CharField(label='Your review',widget=forms.Textarea, max_length=200)
    rating = forms.IntegerField(min_value=1, max_value=5)
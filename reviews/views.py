from django.shortcuts import render, HttpResponseRedirect
from . import forms
from .models import Review

# Create your views here.
def review(request):
    if request.method == 'POST':
        form = forms.ReviewForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data["user_name"]
            review = form.cleaned_data["review"]
            rating = form.cleaned_data["rating"]
            new_obj = Review(user_name=user_name, review=review, rating=rating)
            new_obj.save()
            return HttpResponseRedirect('/thank-you')
    else:
        form = forms.ReviewForm()
    return render(request, 'reviews/review.html',{
        'form': form
    })

def thank_you(request):
    return render(request, 'reviews/thank_you.html')
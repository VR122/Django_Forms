from django.shortcuts import render, HttpResponseRedirect
from . import forms

# Create your views here.
def review(request):
    if request.method == 'POST':
        form = forms.ReviewForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect('/thank-you')
    form = forms.ReviewForm()
    return render(request, 'reviews/review.html',{
        'form': form
    })

def thank_you(request):
    return render(request, 'reviews/thank_you.html')
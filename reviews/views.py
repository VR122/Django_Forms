from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from . import forms

# Create your views here.
class ReviewView(View):
    def get(self, request):
        form = forms.ReviewForm()
        return render(request, 'reviews/review.html',{
                'form': form
            })
    

    def post(self, request):
        form = forms.ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thank-you')
        return render(request, 'reviews/review.html',{
                'form': form
            })

def thank_you(request):
    return render(request, 'reviews/thank_you.html')
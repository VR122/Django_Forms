from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.views import View
from .models import Review
from . import forms

# Create your views here.
class ReviewView(View):
    def get(self, request):
        form = forms.ReviewForm()
        return render(request, 'reviews/review.html',{
                'form': form
            })
    

    def post(self, request):
        user_name = request.POST.get('user_name')
        review = Review.objects.filter(user_name=user_name).first()
        
        if review:
            form = forms.ReviewForm(request.POST, instance=review)
        else:
            form = forms.ReviewForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thank-you')
        
        return render(request, 'reviews/review.html', {
            'form': form
        })

def thank_you(request):
    return render(request, 'reviews/thank_you.html')
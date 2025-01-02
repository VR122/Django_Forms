from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
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


class AllReviewsView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"
    
class ReviewDetailView(DetailView):
    template_name = "reviews/review_detail.html"
    model = Review

class ThankYouTemplateView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "Thank you for submitting your review. Your feedback is important to us."
        return context
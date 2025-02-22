from django.urls import path
from . import views


urlpatterns = [
    path('', views.ReviewView.as_view()),
    path('thank-you', views.ThankYouTemplateView.as_view()),
    path('reviews', views.AllReviewsView.as_view()),
    path('reviews/favorite', views.FavoriteReviewView.as_view()),
    path('reviews/<int:pk>', views.ReviewDetailView.as_view())
]
from . import views
from django.urls import path

urlpatterns = [
   path("", views.reviews, name="reviews"),
   path("form/", views.review_form, name = 'review_form'),
   path("<int:review_id>/", views.review_info, name="review_info")
]
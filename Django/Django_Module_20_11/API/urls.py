from django.urls import path

from . import views
urlpatterns = [
    path("prediction/", views.prediction, name="prediction"),
    path("random-number/", views.random_number, name="random-number")
]
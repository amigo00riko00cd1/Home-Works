from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path("<str:language>", views.index, name="index_parameter")
]
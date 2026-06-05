"""
URL configuration for Django_Modul_20 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path

from main.views import main, news, chapter, facts, management, history, history_people, history_photos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
    path('news/', news, name='news'),
    re_path(r'^news/.*$', news, name='news_detail'),
    path('chapter/', chapter, name='chapter'),
    re_path(r'chapter/.*$', chapter, name='chapter_detail'),
    path('facts/', facts, name='facts'),
    re_path(r'^facts/.*$', facts, name='facts_detail'),
    path('management/', management, name='management'),
    re_path(r'^management/.*$', management, name='management_detail'),
    path('history/', history, name='history'),
    path('history/people/', history_people, name='history_people'),
    path('history/photos/', history_photos, name='history_photos'),

]

from django.urls import path
from . import views

urlpatterns = [
    path("", views.main_page, name="main"),
    path("writers/", views.writers, name="writers"),
    path("writers/<str:surname>/", views.writer_info, name="writer_info"),
    path("topbestbooks/", views.top_best_books, name="top_best_books"),
    path("topbestbooks/<int:topBestBooks>", views.book_info, name="book_info")
]
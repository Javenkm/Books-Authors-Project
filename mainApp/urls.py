from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('books/', views.addBook),
    path('books/<int:id>/', views.viewBook),
    path('authors/', views.addAuthor),
    path('authors/<int:id>/', views.viewAuthor),
    path('books/<int:id>/delete', views.delete_book),
    path('authors/<int:id>/delete', views.delete_author)
    ]
from django.contrib import admin
from django.urls import path
from . import views
from . import models

urlpatterns = [
    path('', views.Home.as_view(), name='books-home'),
    path('booklog/<int:pk>/', views.Detail.as_view(), name='books-detail'),
    path('booklog/create', views.AddBook, name='add-books'),
]

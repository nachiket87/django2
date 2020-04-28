from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from . import models

urlpatterns = [
    path('', views.Home.as_view(), name='books-home'),
    path('booklog/<int:pk>/', views.Detail.as_view(), name='books-detail'),
    path('booklog/create', views.AddBook, name='add-books'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
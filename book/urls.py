from django.urls import path
from . import views

urlpatterns = [
    path('', views.book, name='book'),
    path('search/', views.search, name='search'),
]

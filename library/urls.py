from django.urls import path
from . import views

urlpatterns = [
    path('', views.library, name='library'),
    path('add/<str:isbn>', views.library_add, name='library_add'),
]

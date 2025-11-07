from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_breeds/', views.get_breeds, name='get_breeds'),
    path('get_dog_images/', views.get_dog_images, name='get_dog_images')
]
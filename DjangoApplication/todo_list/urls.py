from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('to-do/', views.To_Do, name = 'To_Do'),
    path('about/', views.about, name = 'about'),
    path('contact/', views.contact, name = 'contact'),
]

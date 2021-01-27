from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('to-do/', views.To_Do, name = 'To_Do'),
    path('about/', views.about, name = 'about'),
    path('contact/', views.contact, name = 'contact'),
    path('delete/<list_id>', views.delete, name='delete'),
    path('complete/<list_id>', views.complete, name='complete'),
    path('incomplete/<list_id>', views.incomplete, name='incomplete'),
]

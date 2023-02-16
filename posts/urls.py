from django.urls import path;
from . import views;

urlpatterns = [
    path('', views.Homego, name='homego'),
    path('about/', views.About, name='About'),
   path('aboutus/',views.Aboutus,name='aboutus'),
   path('services/',views.Services,name='services'),
   path('Home/',views.Home,name='home')
]


from django.urls import path
from django.urls import path, include

from . import views

urlpatterns = [
    path('profile/', views.profile_view, name='profil'),
    path('signup/', views.signup_view, name='rejestracja'),
    path('home/', views.home_view, name='home'),
    path('', views.home_view, name='home'),
    path('', include('django.contrib.auth.urls')),
]
"""carpooling URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
#from accounts.views import home_view, signup_view, profile_view
from drivers.views import add_driver_view, add_passenger_view


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', home_view, name='home'),
    #path('home/', home_view, name='home'),
    #path('signup/', signup_view, name='rejestracja'),
    path('', include('django.contrib.auth.urls')),
    path('add_driver/', add_driver_view, name='dodaj przejazd'),
    path('add_passenger/', add_passenger_view, name='dodaj przejazd'),
    #path('profile/', profile_view, name='profil'),
    path('accounts/', include('accounts.urls'))
]




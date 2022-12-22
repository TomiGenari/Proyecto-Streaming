"""Config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from appStreaming import views
from django.urls import path
from django.conf.urls import include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('register/', views.productor, name='register'),
    path('admin/', admin.site.urls),
    path('', include('appStreaming.urls')),
    path("accounts/", include("django.contrib.auth.urls")), 
    path("", TemplateView.as_view(template_name="main.html"), name="main"),
    path('home/', views.home, name='Inicio'),
    path('main/', views.inicio, name='registro de eventos'),
    path('chose/', views.chose, name='elegir'),
    path("", TemplateView.as_view(template_name="chose.html"), name="chose"),
    path('eventosregistrados/', views.eventosregistrados, name='eventosregistrados'),







]

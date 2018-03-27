"""Tournament URL Configuration

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
from django.urls import path
from django.urls import re_path
from Taekwondo import views

urlpatterns = [
    path('admin/',admin.site.urls),
    re_path(r'^$',views.about,name="Login"),
    path('base.html',views.Home),
    path('login.html/',views.login),
    path('logout.html/',views.logout),
    path('auth/',views.auth_view),
    path('invalid.html/',views.invalid),
    path('about.html/',views.about,name="About"),
    re_path('delete.html/(\d+)/',views.delete,name="Delete"),
    path('add.html/',views.addItem,name="Add"),
    path('player.html/',views.index),
    path('findproduct.html/',views.findproduct,name="find"),
    path('find.html/',views.search,name="search"),
    re_path('del.html/',views.del1,name="Delete1"),
    #re_path(r'^update.html/(\d+)/',views.update,name="Update"),
    path('tour.html/',views.tournament,name="Tournament"),
]


"""text_tute URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from . import view
urlpatterns = [
    # '' are use for index page or daseboard path hae 3 variable >1. name of sub. url 2. function name in main file 3. sortcut of the name 
    
    path('admin/', admin.site.urls),
    path('',view.index,name='index'),
    path('learning1',view.learning1,name='learning1'),
    path('removepunc',view.removepunc,name='removepunc'),
    path('boostrap',view.boostrap,name='boostrap')
]

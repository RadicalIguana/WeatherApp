from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', include('weather.urls')) # Обращаемся к программе weather и берем у нее urls
]

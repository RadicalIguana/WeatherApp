from django.urls import path
from . import views # Из текущей директории испртируем файл views 

urlpatterns = [
    path('', views.index) # При переходе на главную страницу используем фаил views и функцию index
]

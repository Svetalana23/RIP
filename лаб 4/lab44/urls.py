from django.contrib import admin
from django.urls import path
from lab_4 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.GetAnimals, name='home_url'),
    path('details/<int:id>', views.GetAnimal, name='animal_url'),
]

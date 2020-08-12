from django.contrib import admin
from django.urls import path
import mini_project.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('food/', views.food),
    path('stay/', views.stay),
    path('festival/', views.festival),
    path('travel/', views.travel),
]

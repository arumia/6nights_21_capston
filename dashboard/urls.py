from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('write/', views.write),
    path('read/', views.read)
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('sing-up/', views.sing_up),
    path('register/', views.register),
]
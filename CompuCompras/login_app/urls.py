from django.urls import path
from . import views



urlpatterns = [
    path('login/', views.VLogearse.as_view(), name='login'),
    path('sign-up/', views.VRegistrase.as_view(), name='sign-up'),
    path('register/', views.register)    
]
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('login/', views.VLogearse.as_view(), name='login'),
    path('sign-up/', views.VRegistrase.as_view(), name='sign-up'),
    path('register/', views.register),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='password_reset_inicio.html'), name='password_reset'),
    path('reset_password_hecho/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_enviado.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_password.html'), name='password_reset_confirm'),
    path('reset_password_completado/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_hecho.html'), name='password_reset_complete'),

]
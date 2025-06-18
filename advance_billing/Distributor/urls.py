from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('profile/', views.profile, name='profile'),
]

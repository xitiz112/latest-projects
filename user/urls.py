from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'), 
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'), 
    path('training_cost/', views.Training_cost, name='training_cost'),
    
     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
   
]
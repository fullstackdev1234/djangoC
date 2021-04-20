from django.urls import path
from . import views


urlpatterns = [    
    path('register/', views.register ,name='register'),
    path('login/', views.login ,name='login'),
    path('otp', views.otp ,name='otp'),
    path('cfpwd/', views.cfpwd ,name='cfpwd'),
]
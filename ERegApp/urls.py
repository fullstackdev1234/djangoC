from django.urls import path
from . import views


urlpatterns = [    
    path('Eregister/', views.Eregister ,name='Eregister'),
    path('Elogin/', views.Elogin ,name='Elogin'),
    path('Eotp/', views.Eotp ,name='Eotp'),
    path('Efpwd/', views.Efpwd ,name='Efpwd'),
]
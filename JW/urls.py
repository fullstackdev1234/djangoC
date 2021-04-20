"""JW URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index ,name='index'),
    path('contact_us/', views.contact_us ,name='contact_us'),
    path('error/', views.error ,name='error'),  
    path('about_us/', views.about_us ,name='about_us'),
    path('our_services/', views.our_services ,name='our_services'),
    path('privacy/', views.privacy ,name='privacy'),
    path('terms/', views.terms ,name='terms'),
    path('sitemap/', views.sitemap ,name='sitemap'),
    
    path('register/', include('CRegApp.urls')),
    path('jobs/', include('CJobApp.urls')),
    path('resume/', include('CResumeApp.urls')),
    path('blog/', include('CBlogApp.urls')),
    path('pricing/', include('CPricingApp.urls')),
    path('employer/', include('CEmployerApp.urls')),
    path('employer-dashboard/', include('EDashApp.urls')),
    path('employer-register/', include('ERegApp.urls')),
    path('employer-pricing/', include('EPricingApp.urls')),

    path('dashboard/', include('CDashApp.urls')),




]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
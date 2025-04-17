from django.contrib import admin
from django.urls import path
from home import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('index/', views.index, name="index"),
    path('home/', views.home, name="home"),
    path('login/', views.login),
    path('logout/', views.logout),
    path('about/', views.about),
    path('add_property/', views.add_property),
    path('sign_up/', views.sign_up),
    path('contact/', views.contact,name="contact"),
    path('services/', views.services),
    path('company_certification/', views.company_certification),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 






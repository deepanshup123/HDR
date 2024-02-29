from django.contrib import admin
from django.urls import path
from HDRAPP import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name="home"),
    path('register/', views.Register, name='register'),
    path('home/', views.Home, name='home'),
    path('aboutus/', views.AboutUs, name='aboutus'),
    path('upload_video/', views.Video, name='Video'),
    path('video/', views.Video_List, name='Video_List'),
    path('faq/', views.FAQ, name='faq'),
    path('contact/', views.Contact, name='contact'),
    path('services/', views.Services, name='services'),
]
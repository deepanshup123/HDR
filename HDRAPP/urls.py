from django.contrib import admin
from django.urls import path
from HDRAPP import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name="home"),
    path('register', views.Register, name='register'),
    path('home', views.Home, name='home'),

]
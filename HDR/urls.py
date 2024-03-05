"""
URL configuration for HDR project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('HDRAPP.urls')),
    path('register/', include('HDRAPP.urls')),
    path('home/', include('HDRAPP.urls')),
    path('services/', include('HDRAPP.urls')),
    path('aboutus/', include('HDRAPP.urls')),
    path('video/', include('HDRAPP.urls')),
    path('upload_video/', include('HDRAPP.urls')),
    path('user/', include('HDRAPP.urls')),
    path('contact/', include('HDRAPP.urls')),
    path('login/', include('HDRAPP.urls')),
    path('logout/', include('HDRAPP.urls')),
    path('finds/', include('HDRAPP.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

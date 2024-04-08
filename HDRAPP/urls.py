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
    path('user/', views.USER, name='user'),
    path('uservideoedit/<eid>', views.UserVideoEdit, name='uservideoedit'),
    path('uservideodelete/<did>', views.UserVideoDelete, name='uservideodeletet'),
    path('userprofileedit/<upeid>', views.UserProfileEdit, name='userprofileedit'),
    path('userprofiledelete/<upid>', views.UserProfileDelete, name='userprofiledelete'),
    path('contact/', views.Contact, name='contact'),
    path('services/', views.Services, name='services'),
    path('login/', views.Login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('finds/', views.Find, name='finds'),
    path('jform/', views.JoinForm, name='jform'),
    path('otp/<int:rid>/', views.OTP, name='otp'),
    path('search/', views.FilterSearch.as_view(), name='search-list'),
    path('remeber/', views.Remember, name='remember-list'),
    path('addintrest/<int:vid>/', views.add_to_remember, name='addintrest'),
    path('removeintrest/<vrid>', views.RememberDelete, name='removeintrest'),
    path('forgotpass/', views.ForgotPass, name='forgotpass'),
    path('forgotpassotp/<int:fid>/', views.ForgotPassOTP, name='forgotpassotp'),
    path('changepass/<int:cid>/', views.ChangePass, name='changepass'),

]
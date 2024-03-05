from django.shortcuts import render, redirect
from HDRAPP.models import Video_Add
from .forms import User_Video
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as user_login, logout as user_logout
# Create your views here.

def Home(request):
    return render(request, 'HDRAPP/home.html')

def Contact(request):
    return render(request, 'HDRAPP/contact.html')

def Services(request):
    return render(request, 'HDRAPP/services.html')

def AboutUs(request):
    return render(request, 'HDRAPP/aboutus.html')

def USER(request):
    return render(request, 'HDRAPP/faq.html')

def Video(request):
    if request.method == "POST":
        form = User_Video(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'HDRAPP/upload_video.html', {'forms': form})
    return render(request, 'HDRAPP/upload_video.html', {'form': User_Video()})

def Video_List(request):
    videos = Video_Add.objects.all()
    return render(request, 'HDRAPP/video.html', {'videos': videos})

def Register(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        username_check = User.objects.filter(username = username).exists()
        email_check = User.objects.filter(email = email).exists()

        if username_check == True:
            messages.warning(request, 'Username already Exists...')
            return redirect('/register')
        else:
            if email_check == True:
                messages.warning(request, 'Email Already Exists...')
                return redirect('/register')
            else:
                if password != confirm_password:
                    messages.warning(request, 'Password Not Matched...')
                    return redirect('/register')
                else:
                    user = User.objects.create_user(username=username, email=email, password=confirm_password)
                    user.first_name = fname
                    user.last_name = lname
                    user.save()
                    messages.success(request, 'Registration Successfully...')
                    return redirect('/login')
    return render(request, 'HDRAPP/register.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('login_username')
        password = request.POST.get('login_password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            user_login(request, user)
            messages.success(request, 'Login Succefully...')
            return redirect('/')
        else:
            messages.warning(request, 'Check Your Details...')
            return redirect('/login')
    return render(request, 'HDRAPP/login.html')


def logout(request):
    user_logout(request)
    messages.success(request, 'Logout Successfully')
    return redirect('/')

def Find(request):
    return render(request, 'HDRAPP/finds.html')
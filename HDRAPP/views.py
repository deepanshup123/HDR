from django.shortcuts import render
from HDRAPP.models import User_Register, Video_Add
from .forms import User_Video
from django.contrib import messages
# Create your views here.

def Home(request):
    return render(request, 'HDRAPP/home.html')

def Contact(request):
    return render(request, 'HDRAPP/contact.html')

def Services(request):
    return render(request, 'HDRAPP/services.html')

def AboutUs(request):
    return render(request, 'HDRAPP/aboutus.html')

def FAQ(request):
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
        username = request.POST.get('username')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if username and mobile and email and password and confirm_password:
            information = User_Register(username=username, mobile=mobile, email=email, password=password, confirm_password=confirm_password)
            if password == confirm_password:
                information.save()
                messages.success(request, "Profile details updated.")
            else:
                messages.warning(request, "Your Password Not Matched!")
        else:
            messages.warning(request, "Please Fill all the Input Fields")

    return render(request, 'HDRAPP/register.html')


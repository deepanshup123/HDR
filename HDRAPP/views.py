from django.shortcuts import render
from HDRAPP.models import User_Register

from django.contrib import messages
# Create your views here.

def Home(request):
    return render(request, 'HDRAPP/home.html')

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
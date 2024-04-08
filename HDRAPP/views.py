from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from HDRAPP.models import Video_Add, Job_profile, UserVerification, Remembers, ForgetPassword
from .forms import User_Video, Job_Form_Profile
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as user_login, logout as user_logout
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.conf import settings
import random as rn

from django.db.models import Q
from django.views.generic import ListView
# Create your views here.

def Home(request):
    
    
    return render(request, 'HDRAPP/home.html')


def Contact(request):
    context = {}
    if request.user.is_authenticated:
        full_names = request.user.get_full_name()
        context['name'] = full_names
    else:
        context['name'] = "Enter Your Name..."
    if request.method == 'POST':
        full_name = request.POST.get('contact_name')
        mobile_no = request.POST.get('contact_number')
        email = request.POST.get('contact_email')
        text = request.POST.get('contact_text')
        message = f"{text} \n contact:- {mobile_no} \n email: {email}"
        try:
            send_mail(
                subject=full_name,
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
                fail_silently=False
            )
            messages.success(request, "Your Messages Sent Successfully")
            return redirect('contact')
        except Exception:
            messages.warning(request, "Sorry Now Server is Not Reachable")

    return render(request, 'HDRAPP/contact.html', context)

def Services(request):
    return render(request, 'HDRAPP/services.html')

def AboutUs(request):
    return render(request, 'HDRAPP/aboutus.html')

def USER(request):
    context = {}
    userdetails = User.objects.all()
    userVideo = Video_Add.objects.all()
    context['userdetails'] = userdetails
    context['uservideos'] = userVideo
    display_user_video = Video_Add.objects.filter(username = request.user)
    display_user_profiles = Job_profile.objects.filter(username = request.user)
    context['u_video'] = display_user_video
    context['u_profile'] = display_user_profiles
    return render(request, 'HDRAPP/faq.html', context)

def UserVideoEdit(request, eid):
    if request.method == "POST":
        title = request.POST['updatetitle']
        Video_Add.objects.filter(id = eid).update(title = title)
        return redirect('/user')
    else:
        userVideo = Video_Add.objects.filter(id = eid)
        context = {}
        context['vedio_edit'] = userVideo
        return render(request, 'HDRAPP/faqvideoedit.html', context)

def UserProfileEdit(request, upeid):
    if request.method == "POST":
        full_name = request.POST['fname']
        mobile = request.POST['mobn']
        add1 = request.POST['addo']
        add2 = request.POST['addt']
        city = request.POST['city']
        state = request.POST['state']
        zip = request.POST['zip']
        exp = request.POST['exp']
        Job_profile.objects.filter(id = upeid).update(full_name=full_name,mobile_no=mobile,address_one=add1,address_two=add2,city=city, state=state, zip=zip, experience=exp)
        return redirect('/user')
    else:
        userProfile = Job_profile.objects.filter(id = upeid)
        context = {}
        context['up_edit'] = userProfile
        return render(request, 'HDRAPP/job_form_edit.html', context)
    
def UserVideoDelete(request, did):
    delete = Video_Add.objects.filter(id= did)
    delete.delete()
    return redirect('/user')

def UserProfileDelete(request, upid):
    delete = Job_profile.objects.filter(id= upid)
    delete.delete()
    return redirect('/user')


    
def Video(request):
    if request.method == "POST":
        form = User_Video(request.POST, request.FILES)
        if form.is_valid():
            video_add_username = form.save(commit=False)
            video_add_username.username = request.user
            video_add_username.save()
            return redirect('/video')
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
                    start = 100000
                    end = 999999
                    randm = (rn.random() * (end - start + 1)) + start
                    otp = randm.__floor__()
                    user_verification = UserVerification(
                    fname=fname,
                    lname=lname,
                    username=username,
                    email=email,
                    password=password,
                    otp = otp,
                    status = False
                    )
                    username = user_verification.save()
                    id = user_verification.id
                    try:
                        send_mail(
                        subject='HDR OTP Verification',
                        message=f"Your OTP for Registration is {otp}",
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=[email],
                        fail_silently=False
                        )
                        messages.success(request, 'otp sent to your email')
                    except Exception:
                        messages.warning(request, "Sorry Now Server is Not Reachable")
                    return redirect('otp', rid=id)
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
    user_job_profile_data = Job_profile.objects.all()
    context = {
        'data' : user_job_profile_data
    }
    return render(request, 'HDRAPP/finds.html', context)

def JoinForm(request):
    context = {}
    if request.user.is_authenticated:
        full_name = request.user.get_full_name()
        context['name'] = full_name
    else:
        context['name'] = "Enter Your Name..."
    if request.method == "POST":
        form = Job_Form_Profile(request.POST, request.FILES)
        context['forms'] = form

        if form.is_valid():
            job_p_username = form.save(commit=False)
            job_p_username.username = request.user
            username_check = User.objects.filter(username = job_p_username.username).exists()
            if username_check == True:
                messages.warning(request, 'Username already Exists...')
                return redirect('/jform')
            else:
                job_p_username.save()
    else:
        form = Job_Form_Profile()
    context['form'] = Job_Form_Profile()
    return render(request, 'HDRAPP/job_form.html', context)


def Remember(request):
    context = {}
    person_to_remember = Remembers.objects.filter(username = request.user)

    context['data'] = person_to_remember
    return render(request, 'HDRAPP/remember.html', context)

def RememberDelete(request, vrid):
    data = Remembers.objects.filter(id = vrid)
    data.delete()
    return redirect('/remeber')

def add_to_remember(request, vid):
    # print('helo')
    remember_person = Job_profile.objects.get(id = vid)
    user_instance = User.objects.get(username=request.user.username)
    remeber_database = Remembers(
        full_name = remember_person.full_name,
        city = remember_person.city,
        skill = remember_person.skill,
        image = remember_person.image,
        experience = remember_person.experience,
        username=user_instance
    )

    remeber_database.save()
    return redirect('/finds')

# this below is not mendotry
def OTP(request, rid):
    userdata = UserVerification.objects.get(id = rid)
    # print(userdata.password)
    baseotp = userdata.otp
    if request.method == "POST":
        otp = request.POST.get('otp')

        if int(otp) == baseotp:
            user = User.objects.create_user(username=userdata.username, email=userdata.email, password=userdata.password)
            user.first_name = userdata.fname
            user.last_name = userdata.lname
            user.save()
            messages.success(request, 'Registration Successfully...')
            userdata.delete()
            return redirect('login')
        else:
            messages.warning(request, "your Otp not matched please try")
            userdata.delete()
            return redirect('/register')
    else:
        return render(request, 'HDRAPP/otp.html', {'user_data': userdata})


# Search Section
# class SearchView(ListView):
#     model = Job_profile
#     template_name = "HDRAPP/finds.html"
#     queryset = Job_profile.objects.all()
#     context_object_name = 'post'

class FilterSearch(ListView):
    model = Job_profile
    template_name = "HDRAPP/finds.html"
    context_object_name = 'data'

    def get_queryset(self):
        query = self.request.GET.get('search')

        queryset = Job_profile.objects.filter(
        Q(skill__icontains=query) | Q(full_name__icontains=query)
        )

        return queryset.order_by('id')
# user section

def ForgotPass(request):
    if request.method == "POST":
        email = request.POST.get('for_user_mail')
        for_email = User.objects.filter(email = email).exists()
        start = 100000
        end = 999999
        randm = (rn.random() * (end - start + 1)) + start
        otp = randm.__floor__()
        if for_email == True:
            user_email_password = ForgetPassword(
                email = email,
                otp = otp
            )
            user_email_password.save()
            id = user_email_password.id
            name = User.objects.filter(email = email).first()
            fn = name.first_name
            try:
                send_mail(
                subject='Verify Your Email Address Forgotten Password',
                message=f"Dear {fn}, \n\n Thank you for signing up with HDR. To Change your Password, please verify your email address by through OTP : {otp}. \n\n\n Thank You, \n Deepanshu Patel(Founder HDR)",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
                fail_silently=False
                )
                messages.success(request, 'otp sent to your email')
            except Exception:
                messages.warning(request, "Sorry Now Server is Not Reachable")
            return redirect("forgotpassotp", fid =id)
        else:
            messages.warning(request, 'Email not Matched')
    return render(request, 'HDRAPP/forgotpass.html')


def ForgotPassOTP(request, fid):
    if request.method == "POST":
        userotp = request.POST.get('for_user_otp')
        backdata = ForgetPassword.objects.get(id = fid)
        databaseotp = backdata.otp

        if str(userotp) == str(databaseotp):
            messages.success(request, 'Your OTP Matched Successfully')
            return redirect('changepass', cid = fid) 
    return render(request, 'HDRAPP/forgotpassotp.html')


def ChangePass(request, cid):
    userdata = ForgetPassword.objects.filter(id = cid).first()
    email = userdata.email
    print(email)
    if request.method == "POST":
        password = request.POST.get('password')
        conpassword = request.POST.get('confirmpassword')
        if str(password) == str(conpassword):
            user = User.objects.filter(email = email).first()
            user.set_password(conpassword)
            user.save()
            return redirect('login')
    return render(request, 'HDRAPP/changepass.html')
from django import forms
from .models import Video_Add, Job_profile

class User_Video(forms.ModelForm):
    class Meta:
        model = Video_Add
        fields = ['title', 'video']

class Job_Form_Profile(forms.ModelForm):
    class Meta:
        model = Job_profile
        fields = ['full_name', 'mobile_no', 'address_one', 'address_two', 'city', 'state', 'zip', 'skill', 'experience', 'image']
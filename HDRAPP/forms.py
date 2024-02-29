from django import forms
from .models import Video_Add

class User_Video(forms.ModelForm):
    class Meta:
        model = Video_Add
        fields = ['title', 'video']
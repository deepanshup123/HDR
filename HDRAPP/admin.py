from django.contrib import admin

from HDRAPP.models import Video_Add, Job_profile, UserVerification, Remembers, ForgetPassword
# Register your models here.

admin.site.register(Video_Add)
admin.site.register(Job_profile)
admin.site.register(UserVerification)
admin.site.register(Remembers)
admin.site.register(ForgetPassword)

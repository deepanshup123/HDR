from django.db import models

# Create your models here.


class Video_Add(models.Model):
    title = models.CharField(max_length = 200)
    video = models.FileField(upload_to='video/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
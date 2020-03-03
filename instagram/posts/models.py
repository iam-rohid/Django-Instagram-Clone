from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from datetime import date


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images')
    discription = models.TextField()
    uploaded_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.discription[0:100]+"..."

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    image = models.FileField(upload_to='post_images/', blank=False)
    caption = models.TextField(blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.author.username

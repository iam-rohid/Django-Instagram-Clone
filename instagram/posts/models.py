from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models


class Post(models.Model):
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.FileField(upload_to='post_images/', blank=False)
    caption = models.TextField(blank=True)
    uploaded_date = models.DateTimeField(default=timezone.now)

    # def __str__(self):
    # title = self.author.username + " " + self.uploaded_date.strftime('%c')

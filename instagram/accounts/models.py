from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    profile_pic = models.ImageField(
        default='profile_pics/default.jpg', upload_to='profile_pics')

    def fullname(self):
        return f'{self.user.first_name} {self.user.last_name}'

    def __str__(self):
        return f'{self.user.username} profile'


def create_profile(sender, **kwargs):
    userargs = kwargs['instance']
    if kwargs['created']:
        user_profile = Profile.objects.create(user=userargs)


post_save.connect(create_profile, sender=User)

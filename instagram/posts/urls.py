from django.urls import path, include
from .views import add_post

urlpatterns = [
    path('add', add_post, name='add_post')
]

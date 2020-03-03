from django.shortcuts import render, redirect
from .models import Post
from .forms import AddPostForm


def add_post(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return redirect('home')

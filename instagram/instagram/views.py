from django.shortcuts import render, redirect
from posts.models import Post
from posts.forms import AddPostForm


def home(request):
    posts = Post.objects.order_by('-uploaded_date')
    context = {
        'title': 'Instagram',
        'posts': posts,
        'form': AddPostForm,
    }
    return render(request, 'home.html', context)

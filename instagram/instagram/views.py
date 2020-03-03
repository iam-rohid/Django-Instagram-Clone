from django.shortcuts import render, redirect
from posts.models import Post


def home(request):
    posts = Post.objects.order_by('-uploaded_date')
    context = {
        'title': 'Instagram',
        'posts': posts
    }
    return render(request, 'home.html', context)

from django.shortcuts import render, redirect
from posts.models import Post
from posts.forms import AddPostForm
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    posts = Post.objects.order_by('-date_posted')
    context = {
        'title': 'Instagram',
        'posts': posts,
        'form': AddPostForm,
    }
    return render(request, 'home.html', context)

from django.shortcuts import render, redirect
from posts.models import Post
from django.contrib.auth.models import User
from posts.forms import AddPostForm
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    posts = Post.objects.order_by('-date_posted')
    context = {
        'posts': posts,
        'form': AddPostForm,
    }
    return render(request, 'home.html', context)


def profile(request, username):
    thisuser = (User.objects.filter(username=username))
    if len(thisuser) != 0:
        thisuser = thisuser[0]
        posts = Post.objects.filter(author=thisuser).order_by('-date_posted')
        return render(request, 'accounts/profile.html', {'posts': posts, 'thisuser': thisuser, 'title': thisuser.username})
    else:
        return redirect('home')

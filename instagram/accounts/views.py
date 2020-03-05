from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from posts.models import Post
from accounts.models import User


def register(request):
    form = UserRegisterForm()
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


@login_required
def profile(request):
    posts = Post.objects.filter(
        author=request.user.id).order_by('-date_posted')
    context = {
        'posts': posts,
    }
    return render(request, 'accounts/profile.html', context)

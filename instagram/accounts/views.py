from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.db.models.signals import pre_save
from django.contrib.auth.models import User

from posts.models import Post
from .forms import UserRegisterForm


# user register view
def register(request):
    form = UserRegisterForm()
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # Auto user login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            # Redirecting to user's profile page
            return HttpResponseRedirect(f'/{username}/')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form, 'title': 'Sign Up'})


# user logout view
def logout_view(request):
    logout(request)
    return redirect('login')


# user login view
def login_view(request):
    username = password = ''
    context = {
        'error': '',
        'title': 'Log In'
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                # Redirecting to user's profile page
                return HttpResponseRedirect(f'/{username}/')
        else:
            errorUsername = User.objects.filter(username=username)

            if len(errorUsername) != 0:
                context['error'] = "Password didn't match!"
            else:
                context['error'] = "No user found!"
            return render(request, 'accounts/login.html', context)
    else:
        return render(request, 'accounts/login.html', context)

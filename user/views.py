from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import LoginForm
from .models import Profile
from blog.models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


# Create your views here.
@login_required
def profileView(request):
    post = Post.objects.filter(author = request.user)
    return render(request, 'user/profile.html', {'contents': post})


def registerUser(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('loginUser')
    else:
        form = UserCreationForm()
    return render(request, 'user/register.html', {'form': form})


def loginUser(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)
                username = form.cleaned_data.get('username')
                messages.success(request, f'Welcome {username}')
                return redirect('blog-home')
            else:
                messages.error(request, 'Invalid Credentials')
                return redirect('loginUser')
    else:
        form = LoginForm()
    return render(request, 'user/login.html', {'form': form})

def logoutUser(request):
    logout(request)
    messages.success(request, 'Log out success')
    return redirect('loginUser')
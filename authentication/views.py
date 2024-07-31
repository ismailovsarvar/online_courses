from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

from .forms import RegisterForm, LoginForm


def logout_page(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')
    return render(request, 'app/index.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'auth/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.user
            if user:
                login(request, user)
                return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'auth/login.html', {'form': form})



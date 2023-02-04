from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

from users.forms import RegisterForm, LoginForm

def register_view(request):
    form = RegisterForm()
    message = None
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            if password == confirm_password:
                user = form.save(commit=False)
                user.set_password(password)
                user.save()
                login(request, user)
                return redirect('home')
            else:
                message = 'Passwords must match'
    context = {
        'form': form,
        'message': message
    }
    return render(request, 'register-form.html', context)


def login_view(request):
    form = LoginForm()
    message = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                return redirect('home')
            else:
                message = 'Invalid credentials!'
    context = {
        'form': form,
        'message': message
    }
    return render(request, 'login-form.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')
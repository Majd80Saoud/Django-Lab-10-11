from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def register_user(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('register')

        User.objects.create_user(username=username, password=password)

        messages.success(request, 'You have successfully registered')
        return redirect('login')

    return render(request, 'register.html')


def login_user(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successfully')
            return redirect('/books/')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')


def logout_user(request):

    logout(request)
    messages.success(request, 'Logout successfully')
    return redirect('login')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_customs(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect('main')
    else:
        messages.error(request, 'Пользователь не найден или не верный пароль')

    return render(request, 'login.html')

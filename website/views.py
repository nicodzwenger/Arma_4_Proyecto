from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(email=email, username=username, password=password)
            user = User.objects.create_user(email=email, username=username, password=password)
            user.save()
            login(request, user)
            messages.success(request, ("Registro completado!"))
            return redirect('index')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {
        'form':form,
    })



def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.success(request, ("Hubo un error"))
            return redirect('login')

    return render(request, 'login.html', {})


def logout(request):
    logout(request)
    messages.success(request, ("Te has deslogueado"))
    return redirect('index')

def index(request):
    return render(request, 'index.html', {})

def buy(request):
    return render(request, 'buy.html', {})

def terms(request):
    return render(request, 'terms.html', {})

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from accounts.forms import UserRegisterForm

def home_view(request):
    if not request.user.is_authenticated:
        return redirect('register')
    return render(request, 'home.html')

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            response = redirect('home')
            response.set_cookie('registered', True)
            messages.success(request, 'Registration successful.')
            return response
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def contact_view(request):
    return render(request, 'contact.html')

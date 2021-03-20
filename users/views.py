#14.0 Setting up login form 
from django.views import View
from django.contrib.auth import authenticate, login, logout #14.4 
from django.shortcuts import render, redirect, reverse #14.4 
from . import forms

#14.1 Login form 
class LoginView(View):
    def get(self, request):
        form = forms.LoginForm(initial={'email': 'example@example.com'})
        return render(request, 'users/login.html', {'form': form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            #14.4 
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username='email', password='password')
            if user is not None:
                login(request, user)
                return redirect(reverse('core:home'))
        return render(request, 'users/login.html', {'form': form})

#14.4
def log_out(request):
    logout(request)
    return redirect(reverse('core:home'))

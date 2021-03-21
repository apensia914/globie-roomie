from django.views import View
from django.views.generic import FormView
from django.contrib.auth import authenticate, login, logout 
from django.shortcuts import render, redirect, reverse 
from django.urls import reverse_lazy 
from . import forms

# Login View
class LoginView(FormView):
    template_name = 'users/login.html'
    form_class = forms.LoginForm
    success_url = reverse_lazy('core:home') 

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

def log_out(request):
    logout(request)
    return redirect(reverse('core:home'))

# Signup View
class SignUpView(FormView):
    template_name = 'users/signup.html'
    form_class = forms.SignUpForm
    success_url = reverse_lazy('core:home')
    initial = {
        'first_name': 'Donghoon',
        'last_name': 'Han',
        'email': 'example@example.com',
    }

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        user.verify_email() 
        return super().form_valid(form)

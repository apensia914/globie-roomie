#14.0 Setting up login form 
from django.views import View
from django.views.generic import FormView
from django.contrib.auth import authenticate, login, logout #14.4 
from django.shortcuts import render, redirect, reverse #14.4 
from django.urls import reverse_lazy #14.5
from . import forms

#14.1 Login form 
class LoginView(FormView):
    template_name = 'users/login.html'
    form_class = forms.LoginForm
    success_url = reverse_lazy('core:home') #14.5

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

#14.4
def log_out(request):
    logout(request)
    return redirect(reverse('core:home'))

#15.0
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
        return super().form_valid(form)

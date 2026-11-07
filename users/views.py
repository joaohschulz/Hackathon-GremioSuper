from django.shortcuts import render
from django.contrib.auth.views import LoginView as DjangoLoginView, LogoutView as DjangoLogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegisterForm


class LoginView(DjangoLoginView):
    template_name = 'login.html'
class LogoutView(DjangoLogoutView):
    template_name = 'logout.html'
class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    
    


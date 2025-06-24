from django.contrib.auth import login, authenticate
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.mixins import LoginRequiredMixin

class SignupView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'auth/signup.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('post-list')
        return render(request, 'auth/signup.html', {'form': form})

class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'auth/login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('post-list')
        return render(request, 'auth/login.html', {'form': form, 'error': 'Invalid credentials'})


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        auth_logout(request)
        return render(request, 'auth/logout.html')

def LandingPage(request):
    return render(request, 'auth/landing.html', {
        'title': 'Welcome to the Blogging Platform',
        'description': 'A simple blogging platform built with Django.'
    })  
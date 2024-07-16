# authentication/views.py

from django.shortcuts import render, redirect
from django.views import View
from .forms import RegisterForm, AuthenticateForm
from .models import User
import bcrypt

class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
            user.save()
            return redirect('authenticate')
        return render(request, 'register.html', {'form': form})

class AuthenticateView(View):
    def get(self, request):
        form = AuthenticateForm()
        return render(request, 'authenticate.html', {'form': form})

    def post(self, request):
        form = AuthenticateForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data['id']
            dob = form.cleaned_data['dob']
            doa = form.cleaned_data['doa']
            password = form.cleaned_data['password']

            user = User.objects.filter(id=id, dob=dob, doa=doa).first()
            if user and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                return render(request, 'authenticated_page.html')
            else:
                form.add_error(None, 'Invalid credentials')
        return render(request, 'authenticate.html', {'form': form})

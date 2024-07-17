from django.shortcuts import render, redirect
from django.views import View
from .forms import RegisterForm, AuthenticateForm
from .models import User, Recording
from django.core.files.base import ContentFile
from django.http import HttpResponse
import logging
import base64
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
logger = logging.getLogger(__name__)

class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('authenticate')
            except Exception as e:
                logger.error(f"Error during user registration: {e}")
                form.add_error(None, 'An error occurred during registration. Please try again.')
        return render(request, 'register.html', {'form': form})


class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('recording_list')
        return render(request, 'login.html', {'form': form})

class AuthenticateView(View):
    def get(self, request):
        form = AuthenticateForm()
        return render(request, 'ivr_call.html', {'form': form})

    def post(self, request):
        form = AuthenticateForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data['id']
            dob = form.cleaned_data['dob']
            doa = form.cleaned_data['doa']

            try:
                user = User.objects.get(id=id, dob=dob, doa=doa)
                request.session['user_id'] = user.id
                return redirect('recording_page')
            except User.DoesNotExist:
                form.add_error(None, 'Invalid credentials')
        return render(request, 'ivr_call.html', {'form': form})



logger = logging.getLogger(__name__)

class RecordingPage(View):
    def get(self, request):
        return render(request, 'recording_page.html')

    def post(self, request):
        user_id = request.session.get('user_id')
        if not user_id:
            return HttpResponse("User not authenticated", status=401)

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            logger.error("User not found in the database")
            return HttpResponse("User not found", status=404)

        try:
            audio_data = request.POST['audio_file']
            format, audio_str = audio_data.split(';base64,')
            ext = format.split('/')[-1]
            audio_file = ContentFile(base64.b64decode(audio_str), name=f'recording.{ext}')

            recording = Recording(user=user, audio_file=audio_file)
            recording.save()

            return redirect('success_page')
        except Exception as e:
            logger.error(f"Error saving recording: {e}")
            return HttpResponse("An error occurred during file upload", status=500)

class SuccessPage(View):
    def get(self, request):
        return HttpResponse("Recording successfully uploaded!")



class RecordingListView(View):
    def get(self, request):
        recordings = Recording.objects.all()
        return render(request, 'recording_list.html', {'recordings': recordings})



class HomePageView(View):
    def get(self, request):
        return render(request, 'home.html')



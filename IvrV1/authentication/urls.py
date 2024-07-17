from django.urls import path
from .views import RegisterView, AuthenticateView, RecordingPage, SuccessPage

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('authenticate/', AuthenticateView.as_view(), name='authenticate'),
    path('recording_page/', RecordingPage.as_view(), name='recording_page'),
    path('upload_recording/', RecordingPage.as_view(), name='upload_recording'),
    path('success/', SuccessPage.as_view(), name='success_page'),
]

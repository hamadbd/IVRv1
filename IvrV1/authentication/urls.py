from django.urls import path
from .views import RegisterView, AuthenticateView, RecordingPage, SuccessPage, RecordingListView, LoginView, HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('ivr_call/', AuthenticateView.as_view(), name='ivr_call'),
    path('recording_page/', RecordingPage.as_view(), name='recording_page'),
    path('upload_recording/', RecordingPage.as_view(), name='upload_recording'),
    path('success/', SuccessPage.as_view(), name='success_page'),
    path('recordings/', RecordingListView.as_view(), name='recording_list'),
    path('login/', LoginView.as_view(), name='login'),
]

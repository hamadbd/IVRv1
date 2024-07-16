# authentication/urls.py

from django.urls import path
from .views import RegisterView, AuthenticateView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('authenticate/', AuthenticateView.as_view(), name='authenticate'),
]

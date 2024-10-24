from django.urls import path
from django.contrib.auth.views import LoginView
from .views import signup

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('sign_up/', signup, name='SignUp'),
]

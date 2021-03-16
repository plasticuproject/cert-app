# accounts/urls.py
from django.urls import path
from django.views.generic import TemplateView
from .views import SignUpView, ChangePasswordView, password_change_success

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('change/password/',
         ChangePasswordView.as_view(),
         name='change_password'),
    path('change/password/success', password_change_success, name='password_change_success')
]

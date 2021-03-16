# accounts/urls.py
from django.urls import path, re_path

from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('tool/', views.tool, name='tool'),
    path('cert_edit/<cert_id>/', views.cert_edit, name='cert_edit'),
]

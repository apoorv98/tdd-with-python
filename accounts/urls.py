#!/usr/bin/env python3

from django.urls import path
from accounts import views

urlpatterns = [
    path('send_login_email', views.send_login_email, name='send_login_email'),
    path('login?token=abcd123', views.login, name='login'),
]

from django.shortcuts import render
from django.urls import path
from . import views
from App.views import dashboard_view
from django.contrib.auth.views import LoginView

urlpatterns = [
	path('dashboard/', dashboard_view, name="dashboard"),
	path('login/', LoginView.as_view(redirect_authenticated_user=True), name="login_url"),
	path('signup/', views.signupView, name="register_url")
]

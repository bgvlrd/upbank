from django.shortcuts import render
from django.urls import path, include
from . import views
from App.views import dashboard_view
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('dashboard/', dashboard_view, name="dashboard"),
	path('login/', LoginView.as_view(redirect_authenticated_user=True), name="login_url"),
	path('signup/', views.signupView, name="register_url"),
	path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password/password_reset.html'), name="password_reset"),
	path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password/password_reset_done.html'), name='password_reset_done'),
	path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password/password_reset_confirm.html'), name='password_reset_confirm'),
	path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password/password_reset_complete.html'), name='password_reset_complete'),

]

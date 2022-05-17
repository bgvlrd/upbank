from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from App.decorators import anonymous_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

@login_required
def dashboard_view(request, *args, **kwargs):
	return render(request, "dashboard.html", {})

@anonymous_required(redirect_url='/dashboard')
def landing_view(request, *args, **kwargs):
	return render(request, "landing-page.html", {})

#### REDIRECT LINKS
@anonymous_required(redirect_url='/dashboard')
def login_redirect_view(request, *args, **kwargs):
	response = redirect('/accounts/login/')
	return response

@anonymous_required(redirect_url='/dashboard')
def signup_redirect_view(request, *args, **kwargs):
	response = redirect('/accounts/signup/')
	return response

def logout_view(request):
	if request.method == "POST":
		logout(request)
		return redirect('landing_page')
#### END REDIRECT LINKS



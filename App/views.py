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

@login_required
def fund_deposit_view(request, *args, **kwargs):
	return render(request, "fund_deposit.html", {})

@anonymous_required(redirect_url='/dashboard')
def landing_view(request, *args, **kwargs):
	return render(request, "landing-page.html", {})

def contact_us_view(request, *args, **kwargs):
	return render(request, "contact_us.html", {})

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

#@anonymous_required
def resetPasswordView(request, *args, **kwargs):
	return render(request, "reset-password.html", {})



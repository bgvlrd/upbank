from email import message
from django.shortcuts import render, redirect
from django.http import HttpResponse
from UPBank.settings import LOGIN_REDIRECT_URL
from App.forms import LoanerInForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages
from App.decorators import anonymous_required
from .forms import RegistrationForm

# Create your views here.

@anonymous_required(redirect_url='/dashboard')
def login_user(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('dashboard')
		else:
			messages.error(request, "There was an error logging in. Please make sure you typed the correct username and password.")
			return redirect('login_url')
	
	context = {}
	return render(request, 'registration/login.html', context)

def signupView(request):
	if request.method == "POST":
		regform = RegistrationForm(request.POST)
		# regform2 = LoanerInForm(request.POST)
		if regform.is_valid():
			regform.save()
		#	regform2.save()
			messages.success(request, "Account created successfully! You can now log in to your newly-created account!")
			return redirect('login_url')
		#
		else:	
			context = {
				'regform': RegistrationForm(),
				# 'regform2': LoanerInForm(),
				'invalid_name': True
			}
			messages.error(request, "Registration failed. Please follow the guidelines.")
			return render(request, 'registration/register.html', context)
	else:
		# messages.info(request, "If you signed up successfully, you will be automatically redirected to the log-in page in order to use your newly-created account.")
		context = {
			'regform': RegistrationForm(),
			# 'regform2': LoanerInForm()
		}
	return render(request, 'registration/register.html', context)

@anonymous_required(redirect_url='/dashboard')
def forgotPasswordView(request, *args, **kwargs):
	return render(request, "password/password_reset.html", {})



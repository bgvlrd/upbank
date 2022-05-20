from email import message
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from App.forms import LoanerInForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from App.decorators import anonymous_required
from .forms import RegistrationForm
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib.auth import login, authenticate


# Create your views here.

def signupView(request):
	if request.method == "POST":
		regform = RegistrationForm(request.POST)
		# regform2 = LoanerInForm(request.POST)
		if regform.is_valid():
			regform.save()
			# regform2.save()
			messages.success(request, "Account created successfully! You may now log in to your account!")
			return redirect('login_url')
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

@anonymous_required(redirect_url='/dashboard')
def loginView(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('dashboard')
		else:
			# messages.error(request)
			messages.error(request, 'Incorrect username or password!')
			return redirect('login_url')
	
	context = {}
	return render(request, 'registration/login.html', context)



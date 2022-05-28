from email import message
from pickle import FALSE
import re
from wsgiref.util import request_uri
from django.shortcuts import render, redirect
from django.http import HttpResponse
from UPBank.settings import LOGIN_REDIRECT_URL
from App.forms import LoanerInForm
from App.models import LoanerInformation
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages
from App.decorators import anonymous_required
from .forms import RegistrationForm
from django.contrib.auth.models import Group

# Create your views here.

@anonymous_required(redirect_url='/dashboard')
def login_user(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
		else:
			messages.error(request, "There was an error logging in. Please make sure you typed the correct username and password.")
			return redirect('login_url')
	
	context = {}
	return render(request, 'registration/login.html', context)

def signupView(request):
	if request.method == "POST":
		regform = RegistrationForm(request.POST)
		regform2 = LoanerInForm(request.POST)
		print(regform.errors)
		print("RegForm valid? " + str(regform.is_valid()))
		print(regform2.errors)
		print("LoanerForm valid? " + str(regform2.is_valid()))
		if regform.is_valid() and regform2.is_valid():
			user = regform.save()
			print("user.id =", user.id)
			loaner = regform2.save(commit=False) #get regform, don't save yet
			
			#get saved user and store in accountnumber, then save
			loaner.account_number_id = user.id
			print("loaner.account_number_id =", loaner.account_number_id)
			loaner.save()
			regform2.save_m2m()

			# add user to borrower's group
			group, created = Group.objects.get_or_create(name="Borrower")
			user.groups.add(group)
			user.save()

			print(request.POST)

			messages.success(request, "Account created successfully! You can now log in to your newly-created account!")
			return redirect('login_url')
		
		else:	
			context = {
				'regform': RegistrationForm(),
				 'regform2': LoanerInForm(),
				'invalid_name': True
			}
			messages.error(request, "Registration failed. Please follow the guidelines.")
			return render(request, 'registration/register.html', context)
	else:
		# messages.info(request, "If you signed up successfully, you will be automatically redirected to the log-in page in order to use your newly-created account.")
		context = {
			'regform': RegistrationForm(),
			'regform2': LoanerInForm(),
		}
	return render(request, 'registration/register.html', context)

@anonymous_required(redirect_url='/dashboard')
def forgotPasswordView(request, *args, **kwargs):
	return render(request, "password/password_reset.html", {})



from email import message
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from App.decorators import anonymous_required

# Create your views here.

def signupView(request):
	regform = UserCreationForm()
	messages.info(request, "If you signed up successfully, you will be automatically redirected to the log-in page in order to use your newly-created account.")
	if request.method == "POST":
		regform = UserCreationForm(request.POST)
		if regform.is_valid():
			regform.save()
			messages.success(request, "Account created successfully!")
			return redirect('login_url')
		else:
			regform = UserCreationForm()
			return render(request, 'registration/register.html', {'form':regform, 'invalid_name':True})

	return render(request, 'registration/register.html', {'form':regform})

#@anonymous_required
def forgotPasswordView(request, *args, **kwargs):
	return render(request, "forgot-password.html", {})

#@anonymous_required
def resetPasswordView(request, *args, **kwargs):
	return render(request, "reset-password.html", {})

def resetpassword_redirect_view(request, *args, **kwargs):
	response = redirect('/accounts/signup/')
	return response
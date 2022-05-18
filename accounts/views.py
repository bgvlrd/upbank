from email import message
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from App.forms import LoanerInForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from App.decorators import anonymous_required

# Create your views here.

def signupView(request):
	messages.info(request, "If you signed up successfully, you will be automatically redirected to the log-in page in order to use your newly-created account.")
	if request.method == "POST":
		regform = UserCreationForm(request.POST)
		regform2 = LoanerInForm(request.POST)
		if regform.is_valid():
			regform.save()
			regform2.save()
			messages.success(request, "Account created successfully!")
			return redirect('login_url')
		else:
			context = {
				'regform': UserCreationForm(),
				'regform2': LoanerInForm(),
			}
			return render(request, 'registration/register.html', {'form':regform, 'invalid_name':True})
	else:
		context = {
			'regform': UserCreationForm(),
			'regform2': LoanerInForm(),
		}
	return render(request, 'registration/register.html', context)

#@anonymous_required
def forgotPasswordView(request, *args, **kwargs):
	return render(request, "forgot-password.html", {})

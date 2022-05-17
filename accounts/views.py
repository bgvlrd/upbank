from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import LogoutView as logouts

# Create your views here.

def signupView(request):
	regform = UserCreationForm()
	messages.info(request, "If you signed up successfully, you will be automatically redirected to the log-in page in order to use your newly-created account.")
	if request.method == "POST":
		regform = UserCreationForm(request.POST)
		if regform.is_valid():
			regform.save()
			messages.info(request, "We are so thrilled to have you here. Hats off on making an excellent decision. Wanna learn how to use KeepUP? We can teach you how.")
			return redirect('login_url')
		else:
			messages.error(request, "The username or password you entered already exists or is invalid. Please make sure to follow the guidelines as stated.");
			regform = UserCreationForm()

	return render(request, 'registration/register.html', {'form':regform})

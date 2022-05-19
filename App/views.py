from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from App.decorators import anonymous_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

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

@anonymous_required(redirect_url='/dashboard')
def forgotPasswordView(request, *args, **kwargs):
	return render(request, "password_reset.html", {})

#def password_reset_request(request):
#	if request.method == "POST":
#		password_reset_form = PasswordResetForm(request.POST)
#		if password_reset_form.is_valid():
#			data = password_reset_form.cleaned_data['email']
#			associated_users = User.objects.filter(Q(email=data))
#			if associated_users.exists():
#				for user in associated_users:
#					subject = "Password Reset Requested"
#					email_template_name = "password/password_reset_email.txt"
#					c = {
#					"email":user.email,
#					'domain':'127.0.0.1:8000',
#					'site_name': 'Website',
#					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
#					"user": user,
#					'token': default_token_generator.make_token(user),
#					'protocol': 'http',
#					}
#					email = render_to_string(email_template_name, c)
#					try:
#						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
#					except BadHeaderError:
#						return HttpResponse('Invalid header found.')
#					return redirect ("/password_reset/done/")
#	password_reset_form = PasswordResetForm()
#	return render(request=request, template_name="password/password_reset.html", context={"password_reset_form":password_reset_form})

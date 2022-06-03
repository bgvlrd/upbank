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
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import *
from .forms import *
from decimal import *
from datetime import datetime
from datetime import date
from dateutil import relativedelta

# Create your views here.

# Loan calculator is accessible to public, regardless if user is logged in or not
def loan_calculator_view(request, *args, **kwargs):
	return render(request, "loan_calculator.html", {})

@login_required
def dashboard_view(request, *args, **kwargs):
	if request.user.groups.filter(name__in=['Bank Officer']).exists():
		loan_applications = LoanApplication.objects.all()
		loaner_information = []
		loan_specific_details = []


		for i in loan_applications:
			loaner = LoanerInformation.objects.filter(account_number = i.account_no).first()
			loaner_information.append(loaner)

		for i in loan_applications:
			loan = Loan.objects.filter(loan_account_no = i.loan_account_no).first()
			loan_specific_details.append(loan)

		context = {
			'loan_details' : zip(loan_applications, loaner_information, loan_specific_details)
		}
		return render(request, "dashboard.html", context)
	else:
		return redirect('borrower-loanlist')

@login_required
def dashboard_pending_view(request, *args, **kwargs):
	loan_applications = LoanApplication.objects.filter(application_status = "For Review").order_by('date_of_application')
	loaner_information = []
	loan_specific_details = []


	for i in loan_applications:
		loaner = LoanerInformation.objects.filter(account_number = i.account_no).first()
		loaner_information.append(loaner)

	for i in loan_applications:
		loan = Loan.objects.filter(loan_account_no = i.loan_account_no).first()
		loan_specific_details.append(loan)

	context = {
		'loan_details' : zip(loan_applications, loaner_information, loan_specific_details)
	}
	return render(request, "dashboard/dashboard_pending.html", context)

@login_required
def dashboard_approved_view(request, *args, **kwargs):
	loan_applications = LoanApplication.objects.filter(application_status = "Approved").order_by('date_of_application')
	loaner_information = []
	loan_specific_details = []


	for i in loan_applications:
		loaner = LoanerInformation.objects.filter(account_number = i.account_no).first()
		loaner_information.append(loaner)

	for i in loan_applications:
		loan = Loan.objects.filter(loan_account_no = i.loan_account_no).first()
		loan_specific_details.append(loan)

	context = {
		'loan_details' : zip(loan_applications, loaner_information, loan_specific_details)
	}
	return render(request, "dashboard/dashboard_approved.html", context)

@login_required
def dashboard_rejected_view(request, *args, **kwargs):
	loan_applications = LoanApplication.objects.filter(application_status = "Rejected").order_by('date_of_application')
	loaner_information = []
	loan_specific_details = []


	for i in loan_applications:
		loaner = LoanerInformation.objects.filter(account_number = i.account_no).first()
		loaner_information.append(loaner)

	for i in loan_applications:
		loan = Loan.objects.filter(loan_account_no = i.loan_account_no).first()
		loan_specific_details.append(loan)

	context = {
		'loan_details' : zip(loan_applications, loaner_information, loan_specific_details)
	}
	return render(request, "dashboard/dashboard_rejected.html", context)

@login_required
def borrower_information_view(request, pk):
	loan_application = LoanApplication.objects.filter(loan_account_no = pk).first()
	loaner_information = LoanerInformation.objects.filter(account_number = loan_application.account_no).first()
	loan = Loan.objects.filter(loan_account_no = loan_application.loan_account_no).first()

	if request.method == 'POST':
		if "approve_loan" in request.POST:
			loan_application.application_status = "Approved"
			loan.next_pay_date = date.today() + relativedelta.relativedelta(months=+1)
			loan_application.save()
			loan.save()
			messages.success(request, "Loan successfully approved!")

		elif "reject_loan" in request.POST:
			rejection_reason = request.POST.get('rejection_reason')
			loan_application.rejection_reason = rejection_reason
			loan_application.application_status = "Rejected"
			loan_application.save()
			messages.success(request, "Loan successfully rejected!")
		
		return redirect('dashboard')

	context = {
		'loan_application' : loan_application,
		'loaner_information' : loaner_information,
		'loan' : loan,
	}

	return render(request, "borrower_information.html", context)

@login_required
def fund_deposit_view(request, *args, **kwargs):
	acct = BankAccount.objects.filter(account_number=request.user.id).values()[0]
	user_name = User.objects.filter(id=request.user.id).values_list('first_name', 'last_name')[0]

	full_name = user_name[0] + " " + user_name[1]
	context = {
		'bank_account' : acct,
		'full_name' : full_name
	}
	
	return render(request, "fund_deposit.html", context)


@csrf_exempt
def add_deposit(request):
	if request.method == 'POST':
		amt = request.POST.get('amt')
		
		acct = BankAccount.objects.get(account_number=request.user.id)
		acct.balance += Decimal(amt)
		acct.save()

		user_name = User.objects.filter(id=request.user.id).values_list('first_name', 'last_name')[0]
		full_name = user_name[0] + " " + user_name[1]

		today = datetime.now()
		
		context = JsonResponse({
			'account_number': acct.account_number_derived,
			'amt_deposited': amt,
			'balance': acct.balance,
			'full_name' : full_name,
			'date': today.strftime("%B %d, %Y"),
			'time': today.strftime("%H:%M:%S %p")
		})

		return context

	return HttpResponse(status=500)
		

# Borrower's Views
@login_required
def borrower_loanlist(request):
	loanapplications = LoanApplication.objects.filter(account_no = request.user).order_by('date_of_application')
	loanlist = []
	for i in loanapplications:
		loan = Loan.objects.get(loan_account_no = i.loan_account_no)
		loanlist.append(loan)
	
	context = {
		'myloans' : zip(loanapplications, loanlist)
	}
	return render(request, "borrower_loan_pages/borrower_loanlist.html", context)

@login_required
def loan_information_view(request, accno):
	try:
		loanapp = LoanApplication.objects.get(account_no = request.user, loan_account_ref_no = accno)
		loan = Loan.objects.get(loan_account_no = loanapp.loan_account_no)
	except:
		messages.error(request, "Access denied or the page does not exist!")
		return redirect('borrower-loanlist')
	else:
		context = {
			'loanapp' : loanapp,
			'loan' : loan
		}
		return render(request, "borrower_loan_pages/loan_information.html", context)

@login_required
def applyforLoan(request):
	if request.method == "POST":
		user = request.user
		missing_loanappformfields = LoanApplication(account_no = user)

		loanappform = LoanApplicationForm(request.POST, instance = missing_loanappformfields)
		if loanappform.is_valid():
			loanappobject = loanappform.save()

			interestRate = {
				12 : 0.0558,
				18 : 0.0815,
				24 : 0.1102,
				36 : 0.1690,
				48 : 0.2296,
				60 : 0.2876
			}

			interestRateDatabase = {
				12 : 5.58,
				18 : 8.15,
				24 : 11.02,
				36 : 16.90,
				48 : 22.96,
				60 : 28.76
			}
			
			#Loan Computations
			downpaymentAmount = Decimal(request.POST['selling_prize']) * (Decimal(request.POST['downpayment_percent']) / 100)
			amountFinanced = Decimal(request.POST['selling_prize']) - downpaymentAmount
			basicAmortization = amountFinanced / Decimal(request.POST['total_term'])
			monthlyInterest = (amountFinanced * Decimal(interestRate[int(request.POST['total_term'])])) / Decimal(request.POST['total_term'])
			monthlyAmortization = basicAmortization + monthlyInterest
			
			missing_loanformfields = Loan(
				loan_account_no = loanappobject,
				term_remaining = request.POST['total_term'],
				downpayment = downpaymentAmount,
				aor = interestRateDatabase[int(request.POST['total_term'])],
				monthly_amortization = monthlyAmortization,
				amount_financed = amountFinanced
				)
			loanform = LoanForm(request.POST, instance = missing_loanformfields)
			
			if loanform.is_valid():
				loanform.save()

				messages.success(request, "Loan Application has been added successfully! A Bank Officer will review your application.")
				return redirect('borrower-loanlist')
			else:
				messages.error(request, "Internal error! Please enter the necessary fields correctly!")
				loanappobject.delete()
				context = {
					'loanappform' : loanappform,
					'loanform' : loanform
				}
		else:
			messages.error(request, "Internal error! Please enter the necessary fields correctly!")
			context = {
					'loanappform' : loanappform,
					'loanform' : loanform
				}
	else:
		loanappform = LoanApplicationForm()
		loanform = LoanForm()

		context = {
			'loanappform' : loanappform,
			'loanform' : loanform
		}
	return render(request, "borrower_loan_pages/loan_application.html", context)

@login_required
def otc_payment(request, *args, **kwargs):
	now = datetime.now()
	transaction_date = now.strftime("%B %d, %Y")

	valid_otc_payer = Loan.objects.filter(loan_tag="Delinquent") | Loan.objects.filter(loan_tag="In Loan Default")

	form = OTCPayForm()

	context = {
		'transaction_date' : transaction_date,
		'valid_otc_payer': valid_otc_payer,
		'form': form
	}
	return render(request, "otc_payment.html", context)


@csrf_exempt
def add_otc_payment(request):
	if request.method == 'POST':
		loan_account_no = request.POST.get('loan_account_no')


		loan_account_id = LoanApplication.objects.get(loan_account_ref_no = loan_account_no).loan_account_no
		loan_account = Loan.objects.get(loan_account_no=loan_account_id)

		monthly_amortization = loan_account.monthly_amortization
		months_missed = loan_account.months_missed_counter
		to_pay = monthly_amortization * months_missed

		today = datetime.now()

		context = JsonResponse({
			'to_pay': to_pay,
			'months_missed': months_missed,
			'monthly_amortization': monthly_amortization,
			'loan_account_no': loan_account_no,
			'date': today.strftime("%B %d, %Y"),
			'time': today.strftime("%H:%M:%S %p")
		})

		return context

	return HttpResponse(status=500)

@csrf_exempt
def confirm_otc_payment(request):
	if request.method == 'POST':
		loan_account_no = request.POST.get('loan_account_no')
		print(loan_account_no)

		loan_account_id = LoanApplication.objects.get(loan_account_ref_no = loan_account_no).loan_account_no
		loan_account = Loan.objects.get(loan_account_no=loan_account_id)

		monthly_amortization = loan_account.monthly_amortization
		months_missed = loan_account.months_missed_counter
		to_pay = monthly_amortization * months_missed

		# Continue loan since it is already paid
		loan_account.loan_tag = 'Ongoing'
		loan_account.save()
		loan_account.term_remaining = loan_account.term_remaining - loan_account.months_missed_counter
		loan_account.save()
		loan_account.months_missed_counter = 0
		loan_account.save()

		today = datetime.now()

		context = JsonResponse({
			'to_pay': to_pay,
			'loan_account_no': loan_account_no,
		})

		return context

	return HttpResponse(status=500)

# Landing
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

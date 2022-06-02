from background_task import background
from .models import BankAccount, Loan, LoanApplication, LoanerInformation
from datetime import datetime
from datetime import date

@background(schedule=60)
def collect_loan():
    loans = Loan.objects.all()
    for loan in loans:
    	loan_info = LoanApplication.query.filter(loan_account_no = loan.loan_account_no).first()
    	bank_account = BankAccount.query.filter(account_number = loan_info.account_no).first()

    	if loan.next_pay_date == datetime.now():
    		if bank_account.balance >= loan.monthly_amortization:
	    		bank_account.balance -= bank_account.balance - loan.monthly_amortization
	    		bank_account.save()

	    		loan.term_remaining -= 1
	    		loan.next_pay_date = date.today() + relativedelta(months=+1)
	    		loan.save()

	    	else:
	    		if loan.monthly_missed_counter <= 2:
	    			loan.monthly_missed_counter += 1
	    			loan.loan_tag = loan.loan_tag_choices[1]
	    			loan.next_pay_date = date.today() + relativedelta(months=+1)
	    			loan.save()

	    			bank_account.bank_status = bank_account.bank_status_choices[1]
	    			bank_account.save()
	    		
	    		else:
	    			loan.loan_tag = loan.loan_tag_choices[2]
	    			loan.next_pay_date = date.today() + relativedelta(months=+1)
	    			loan.save()

	    if loan.term_remaining == 0:
	    	loan.loan_tag = loan.loan_tag_choices[0]
	    	loan.save()


    	
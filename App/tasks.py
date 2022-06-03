# from background_task import background
# from .models import BankAccount, Loan, LoanApplication, LoanerInformation
# from datetime import datetime
# from datetime import date
# from dateutil import relativedelta

# @background(schedule=10)
# # @background(schedule=timedelta(hours=24))
# def collect_loan():
# 	loans = Loan.objects.all()
# 	for loan in loans:
# 		loan_info = LoanApplication.objects.filter(loan_account_no = loan.loan_account_no.loan_account_no).first()
# 		bank_account = BankAccount.objects.filter(account_number = loan_info.account_no).first()

# 		print(loan.next_pay_date)
# 		print(date.today())
# 		if loan.next_pay_date == date.today() and loan.months_missed_counter <= 2 and loan_info.application_status == "Approved":
# 			if bank_account.balance >= loan.monthly_amortization:
# 				bank_account.balance -= loan.monthly_amortization
# 				bank_account.save()

# 				loan.loan_tag = "Ongoing"
# 				loan.term_remaining -= 1
# 				loan.next_pay_date = date.today() + relativedelta(months=+1)
# 				loan.save()
# 				print("\nCOLLECTED\n")

# 			else:
# 				if loan.months_missed_counter <= 2:
# 					loan.months_missed_counter += 1
# 					loan.loan_tag = "Delinquent"
# 					loan.next_pay_date = date.today() + relativedelta(months=+1)
# 					loan.save()

# 					bank_account.bank_status = bank_account.bank_status_choices[1]
# 					bank_account.save()

# 				else:
# 					loan.loan_tag = "In Loan Default"
# 					loan.next_pay_date = date.today() + relativedelta(months=+1)
# 					loan.save()

# 		if loan.term_remaining == 0:
# 			loan.loan_tag = "Completed"
# 			loan.save()
# 	print("\nFINISH COLLECT LOAN\n")
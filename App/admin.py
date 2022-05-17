from django.contrib import admin
from .models import BankAccount, LoanerInformation, PersonalReferences, CreditBankReferences, LoanApplication, Loan, OTCPayment

# Register your models here.

class BankAccountTable(admin.ModelAdmin):
    list_display = ('account_number', 'balance', 'bank_status')

class LoanerInformationTable(admin.ModelAdmin):
    list_display = ('account_number', 'full_name')

class PersonalReferencesTable(admin.ModelAdmin):
    list_display = ('personal_reference_id', 'account_number', 'reference_name', 'reference_address', 'reference_contact_number')

class CreditBankReferencesTable(admin.ModelAdmin):
    list_display = ('credit_bank_reference_id', 'account_number', 'bank_name')

class LoanApplicationTable(admin.ModelAdmin):
    list_display = ('loan_account_no', 'account_no', 'date_of_application', 'application_status')

class LoanTable(admin.ModelAdmin):
    list_display = ('loan_account_no', 'amount_financed', 'total_term', 'term_remaining', 'monthly_amortization', 'months_missed_counter', 'loan_tag')

class OTCPaymentTable(admin.ModelAdmin):
    list_display = ('otc_payment_id', 'loan_account_no', 'transaction_date', 'amount_paid')


admin.site.register(BankAccount, BankAccountTable)
admin.site.register(LoanerInformation, LoanerInformationTable)
admin.site.register(PersonalReferences, PersonalReferencesTable)
admin.site.register(CreditBankReferences, CreditBankReferencesTable)
admin.site.register(LoanApplication, LoanApplicationTable)
admin.site.register(Loan, LoanTable)
admin.site.register(OTCPayment, OTCPaymentTable)

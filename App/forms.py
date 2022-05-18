from dataclasses import field, fields
from msilib.schema import MoveFile
from statistics import mode
from django import forms
from django.forms import ModelForm
from App.models import *

class BankAccForm(ModelForm):
    class Meta:
        model = BankAccount
        fields = '__all__'

class LoanerInfForm(ModelForm):
    class Meta:
        model = LoanerInformation
        fields = '__all__'

class PersonalRefForm(ModelForm):
    class Meta:
        model = PersonalReferences
        fields = "__all__"

class CreditBankRefForm(ModelForm):
    class Meta:
        model = CreditBankReferences
        fields = '__all__'

class LoanAppForm(ModelForm):
    class Meta:
        model = LoanApplication
        fields = '__all__'

class LoanForm(ModelForm):
    class Meta:
        model = Loan
        fields = '__all__'

class OTCPayForm(ModelForm):
    class Meta:
        model = OTCPayment
        fields = '__all__'

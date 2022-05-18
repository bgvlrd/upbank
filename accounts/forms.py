from django import forms
from App.models import LoanerInformation

#for registration, just render UserCreationForm 
# and edited LoanerInForm here one after the other. 
# Django knows how to update each form. 
# Source: https://stackoverflow.com/questions/27968417/django-form-with-fields-from-two-different-models

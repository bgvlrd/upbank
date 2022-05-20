from dataclasses import field
from pyexpat import model
from django.forms import ModelForm
from App.models import *

class LoanApplicationForm(ModelForm):
    class Meta:
        model = LoanApplication
        exclude = ['account_no', 'application_status']

class LoanForm(ModelForm):
    class Meta:
        model = Loan
        exclude = ['loan_account_no', 'loan_tag', 'term_remaining', 'months_missed_counter']

class BankAccForm(ModelForm):
    class Meta:
        model = BankAccount
        fields = '__all__'

class LoanerInForm(ModelForm):
    class Meta:
        model = LoanerInformation
        fields = [
            'full_name',
            'gender',
            'nationality',
            'residency',
            'birthdate',
            'birthplace',
            'educational_attainment',
            'civil_status',
            'tin',
            'sss_gsis_no',
            'present_address',
            'prev_address',
            'home_ownership',
            'length_of_stay_years',
            'length_of_stay_months',
            'telephone_no',
            'cellphone_no',
            'email_address',
            'source_of_income',
            'status_of_employment',
        ]

class LoanerInCards(ModelForm):
    class Meta:
        model = LoanerInformation
        fields = [
            'card1_company',
            'card1_number',
            'card1_expiry_date',
            'card1_credit_limit',
            'card1_outstanding_balance',
            'card2_company',
            'card2_number',
            'card2_expiry_date',
            'card2_credit_limit',
            'card2_outstanding_balance'
        ]

class LoanerInFormSpouse(ModelForm):
    class Meta:
        model = LoanerInformation
        fields = [
            'spouse_full_name',
            'spouse_gender',
            'spouse_nationality',
            'spouse_residency',
            'spouse_birthdate',
            'spouse_birthplace',
            'spouse_educational_attainment',
            'spouse_civil_status',
            'spouse_tin',
            'spouse_sss_gsis_no',
            'spouse_source_of_income',
            'spouse_status_of_employment',
            'spouse_company_name',
            'spouse_office_address',
            'spouse_company_web_address',
            'spouse_nature_of_business',
            'spouse_job_title',
            'spouse_company_position',
            'spouse_job_length_of_stay_years',
            'spouse_job_length_of_stay_months',
            'spouse_office_phone_no',
            'spouse_business_name',
            'spouse_business_address',
            'spouse_business_web_address',
            'spouse_nature_of_business_work',
            'spouse_job_length_of_operation_years',
            'spouse_job_length_of_operation_months',
            'spouse_name_prevemployer_business',
            'spouse_country_of_destination',
            'spouse_employment_base'

        ]

class LoanerInFormEmployed(ModelForm):
    class Meta:
        model = LoanerInformation
        fields = [
            'company_name',
            'office_address',
            'company_web_address',
            'nature_of_business',
            'job_title',
            'company_position',
            'job_length_of_stay_years',
            'job_length_of_stay_months',
            'office_phone_no'
        ]

class LoanerInFormBusiness(ModelForm):
    class Meta:
        model = LoanerInformation
        fields = [
            'business_name',
            'business_address',
            'business_web_address',
            'nature_of_business_work',
            'job_length_of_operation_years',
            'job_length_of_operation_months',
            'name_prevemployer_business'
        ]

class LoanerInFormOFW(ModelForm):
    class Meta:
        model = LoanerInformation
        fields = [
            'country_of_destination',
            'employment_base',
        ]

class LoanerInFormDependents(ModelForm):
    class Meta:
        model = LoanerInformation
        fields = [
            'dependent1_name',
            'dependent1_school',
            'dependent1_age',
            'dependent1_level',
            'dependent1_type_of_school',
            'dependent2_name',
            'dependent2_school',
        ]

class LoanerInFormStatement(ModelForm):
    class Meta:
        model = LoanerInformation
        fields = [
            'borrower_monthly_income',
            'borrower_monthly_expenses',
            'spouse_monthly_income',
            'spouse_monthly_expenses'
        ]

class LoanerInFormAssets(ModelForm):
    class Meta:
        model = LoanerInformation
        fields = [
            'cash_hand_with_banks_details',
            'cash_hand_with_banks_amount',
            'real_estate_property_details',
            'real_estate_property_amount',
            'motor_vehicle_details',
            'motor_vehicle_amount',
        ]

class LoanerInFormLiabilities(ModelForm):
    class Meta:
        model = LoanerInformation
        fields = [
            'personal_salary_loan_bank',
            'personal_salary_loan_amortization',
            'personal_salary_loan_outstanding_balance',
            'car_loan_bank',
            'car_loan_amortization',
            'car_loan_outstanding_balance',
            'housing_loan_bank',
            'housing_loan_amortization',
            'housing_loan_outstanding_balance',
        ]

class LoanerInFormOthers(ModelForm):
    class Meta:
        model = LoanerInformation
        fields = [
            'source_product_info',
            'relative_working',
            'relative_name'
        ]

class PersonalRefForm(ModelForm):
    class Meta:
        model = PersonalReferences
        fields = "__all__"

class CreditBankRefForm(ModelForm):
    class Meta:
        model = CreditBankReferences
        fields = '__all__'

class OTCPayForm(ModelForm):
    class Meta:
        model = OTCPayment
        fields = '__all__'

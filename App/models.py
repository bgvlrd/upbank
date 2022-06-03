from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
import random

class BankAccount(models.Model):
    # Create a 9-digit unique account number
    def create_unique_number():
        not_unique = True
        while not_unique:
            unique_no = random.randint(100000000, 999999999)
            if not BankAccount.objects.filter(account_number_derived=unique_no):
                not_unique = False
        return str(unique_no)

    account_number = models.OneToOneField(User, on_delete = models.CASCADE, primary_key=True)
    balance        = models.DecimalField(max_digits = 11, decimal_places = 2)
    account_number_derived = models.CharField(max_length=8, blank=True, editable=False, unique=True, null=True, default=create_unique_number)
    
    def save(self, *args, **kwargs):
        super(BankAccount, self).save(*args, **kwargs)
        user = User.objects.get(bankaccount__account_number=self.account_number)
        self.account_number_derived = str(abs(hash(user.username)))[0:11]
        super(BankAccount, self).save(*args, **kwargs)

    def __str__(self):
        return f'Account ID {self.account_number_derived}'


    bank_status_choices = [
        ('Active', 'Active'),
        ('Closed', 'Closed')
    ]
    
    bank_status     = models.CharField(choices = bank_status_choices, max_length = 10)

class LoanerInformation(models.Model):
    account_number = models.OneToOneField(User, on_delete = models.CASCADE)

    gender_choices = [
		('Male', 'Male'),
		('Female', 'Female')
	]

    residency_choices = [
        ('Resident', 'Resident'),
		('Non-Resident', 'Non-Resident')
    ]

    educational_attainment_choices = [
        ('Elementary', 'Elementary'),
		('High School', 'High School'),
        ('Vocational', 'Vocational'),
        ('College Studies', 'College Studies'),
        ('College (Undergraduate Degree)','College (Undergraduate Degree)'),
        ('College (Postgraduate Degree)', 'College (Postgraduate Degree)'),
    ]

    civil_status_choices = [
        ('Single', 'Single'),
		('Married', 'Married'),
        ('Legally Separated', 'Legally Separated'),
        ('Widow/Widower', 'Widow/Widower')
    ]

    home_ownership_choices = [
        ('Owned', 'Owned'),
		('Mortgaged', 'Mortgaged'),
        ('Rented', 'Rented'),
        ('Living with Parents/Relatives', 'Living with Parents/Relatives')
    ]

    pref_mailing_add_choices = [
        ('Residence', 'Residence'),
		('Office Address', 'Office Address'),
        ('Business Address', 'Business Address')
    ]

    full_name			    = models.CharField(max_length = 200) 
    gender			        = models.CharField(max_length = 10, choices = gender_choices)
    nationality             = models.CharField(max_length = 50)
    residency               = models.CharField(choices = residency_choices, max_length = 15, blank = True, null = True)
    birthdate               = models.DateField()
    def calculate_loaner_age(self):
        today = date.today()
        return today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
    
    birthplace              = models.CharField(max_length = 50)
    educational_attainment  = models.CharField(choices = educational_attainment_choices, max_length = 30, blank = True, null = True)
    civil_status            = models.CharField(choices = civil_status_choices, max_length = 20, blank = True, null = True)
    tin                     = models.CharField(max_length = 10, verbose_name = "Tax Identification Number (TIN)")
    sss_gsis_no             = models.CharField(max_length = 20, verbose_name = "SSS / GSIS Number", blank = True, null = True)
    present_address         = models.CharField(max_length = 500)
    prev_address            = models.CharField(max_length = 500, verbose_name = "Previous Address")
    home_ownership          = models.CharField(choices = home_ownership_choices, max_length = 30, blank = True, null = True)
    length_of_stay_years    = models.IntegerField(blank = True, null = True, verbose_name = "Length of Stay (Years)")
    length_of_stay_months   = models.IntegerField(blank = True, null = True, verbose_name = "Length of Stay (Months)")
    telephone_no            = models.CharField(max_length=20, verbose_name = "Residential Telephone Number")
    cellphone_no            = models.CharField(max_length=15, verbose_name = "Cellphone Number")
    email                   = models.EmailField()
    # pref_mailing_add        = models.CharField(choices = pref_mailing_add_choices, verbose_name = "Preferred Mailing Address")
    
    # Loaner Employment Information

    source_of_income_choices = [
        ('Locally Employed - Private', 'Locally Employed - Private'),
		('Locally Employed - Government', 'Locally Employed - Government'),
        ('Locally Employed - Self-employed', 'Locally Employed - Self-employed'),
        ('OFW Immigrant - Private', 'OFW Immigrant - Private'),
		('OFW Immigrant - Government', 'OFW Immigrant - Government'),
        ('OFW Immigrant - Self-employed', 'OFW Immigrant - Self-employed'),
        ('OFW Non-Immigrant - Private', 'OFW Non-Immigrant - Private'),
		('OFW Non-Immigrant - Government', 'OFW Non-Immigrant - Government'),
        ('OFW Non-Immigrant - Self-employed', 'OFW Non-Immigrant - Self-employed'),
        ('Unemployed - Remittance/Allottee', 'Unemployed - Remittance/Allottee'),
        ('Unemployed - Pension/Retired', 'Unemployed - Pension/Retired'),
        ('Unemployed - Student', 'Unemployed - Student'),
        ('Others', 'Others')
    ]

    status_of_employment_choices = [
        ('Permanent', 'Permanent'),
        ('Probationary', 'Probationary'),
        ('Contractual', 'Contractual')
    ]
    
    company_position_choices = [
        ('Non-Officer', 'Non-Officer'),
        ('Jr. Officer', 'Jr. Officer'),
        ('Supervisor', 'Supervisor'),
        ('Middle Manager', 'Middle Manager'),
        ('Sr. Officer', 'Sr. Officer')
    ]

    source_of_income            = models.CharField(choices = source_of_income_choices, max_length = 50)
    status_of_employment        = models.CharField(choices = status_of_employment_choices, max_length = 15, blank = True, null = True)

    #If employed,
    company_name                = models.CharField(max_length = 100, blank = True, null = True)
    office_address              = models.CharField(max_length = 500, blank = True, null = True)
    company_web_address         = models.CharField(max_length = 100, blank = True, null = True, verbose_name = "Company Website Address")
    nature_of_business          = models.CharField(max_length = 100, blank = True, null = True)
    job_title                   = models.CharField(max_length = 50, blank = True, null = True)
    company_position            = models.CharField(choices = company_position_choices, max_length = 20, blank = True, null = True)
    job_length_of_stay_years    = models.IntegerField(blank = True, null = True, verbose_name = "Length of Stay (Years)")
    job_length_of_stay_months   = models.IntegerField(blank = True, null = True, verbose_name = "Length of Stay (Months)")
    office_phone_no             = models.CharField(max_length = 50, blank = True, null = True, verbose_name = "Office Phone / Fax Number")

    #If in business or in practice of profession,
    business_name                   = models.CharField(max_length = 100, blank = True, null = True)
    business_address                = models.CharField(max_length = 500, blank = True, null = True)
    business_web_address            = models.CharField(max_length = 100, blank = True, null = True, verbose_name = "Business Website Address")
    nature_of_business_work         = models.CharField(max_length = 50, blank = True, null = True, verbose_name = "Nature of Business / Work")
    job_length_of_operation_years   = models.IntegerField(blank = True, null = True, verbose_name = "Length of Operation (Years)")
    job_length_of_operation_months  = models.IntegerField(blank = True, null = True, verbose_name = "Length of Operation (Months)")

    name_prevemployer_business      = models.CharField(max_length = 100, blank = True, null = True, verbose_name = "Name of Previous Employer / Business")

    # If OFW,
    employment_base_choices = [
        ('Land', 'Land'),
		('Sea', 'Sea'),
        ('Air', 'Air')
    ]

    country_of_destination          = models.CharField(max_length = 100, blank = True, null = True)
    employment_base                 = models.CharField(choices = employment_base_choices, max_length = 5, blank = True, null = True)

    # Dependents
    type_of_school_choices = [
        ('Public', 'Public'),
		('Exclusive', 'Exclusive'),
        ('Private Coed', 'Private Coed')
    ]

    # Dependent 1
    dependent1_name                 = models.CharField(max_length = 100, blank = True, null = True, verbose_name = "Name")
    dependent1_school               = models.CharField(max_length = 100, blank = True, null = True, verbose_name = "School")
    dependent1_age                  = models.IntegerField(blank = True, null = True, verbose_name = "Age")
    dependent1_level                = models.CharField(max_length = 100, blank = True, null = True, verbose_name = "Level")
    dependent1_type_of_school       = models.CharField(choices = type_of_school_choices, max_length = 15, blank = True, null = True, verbose_name = "Type of School")

    # Dependent 2
    dependent2_name                 = models.CharField(max_length = 100, blank = True, null = True, verbose_name = "Name")
    dependent2_school               = models.CharField(max_length = 100, blank = True, null = True, verbose_name = "School")
    dependent2_age                  = models.IntegerField(blank = True, null = True, verbose_name = "Age")
    dependent2_level                = models.CharField(max_length = 100, blank = True, null = True, verbose_name = "Level")
    dependent2_type_of_school       = models.CharField(choices = type_of_school_choices, max_length = 15, blank = True, null = True, verbose_name = "Type of School")

    # Information of Spouse
    # Haven't put labelled fields that as "not required" kasi pano pag wala namang spouse si applicant

    spouse_full_name			    = models.CharField(max_length = 200, blank = True, null = True, verbose_name = "Full Name") 
    spouse_gender			        = models.CharField(max_length = 10, blank = True, null = True, choices = gender_choices, verbose_name = "Gender")
    spouse_nationality              = models.CharField(max_length = 50, blank = True, null = True, verbose_name = "Nationality")
    spouse_residency                = models.CharField(choices = residency_choices, max_length = 15, blank = True, null = True, verbose_name = "Residency")
    spouse_birthdate                = models.DateField(blank = True, null = True, verbose_name = "Birthdate")
    def calculate_spouse_age(self):
        today = date.today()
        return today.year - self.spouse_birthdate.year - ((today.month, today.day) < (self.spouse_birthdate.month, self.spouse_birthdate.day))
    
    spouse_birthplace               = models.CharField(max_length = 50, blank = True, null = True, verbose_name = "Birthplace")
    spouse_educational_attainment   = models.CharField(choices = educational_attainment_choices, max_length = 30, blank = True, null = True, verbose_name = "Educational Attainment")
    spouse_civil_status             = models.CharField(choices = civil_status_choices, max_length = 20, blank = True, null = True, verbose_name = "Civil Status")
    spouse_tin                      = models.CharField(max_length = 10, blank = True, null = True, verbose_name = "Tax Identification Number (TIN)")
    spouse_sss_gsis_no              = models.CharField(max_length = 20, blank = True, null = True, verbose_name = "SSS / GSIS Number")

    # Employment Information of Spouse
    spouse_source_of_income            = models.CharField(choices = source_of_income_choices, max_length = 50, blank = True, null = True, verbose_name = "Source of Income")
    spouse_status_of_employment        = models.CharField(choices = status_of_employment_choices, max_length = 15, blank = True, null = True, verbose_name = "Status of Employment")

    # If employed,
    spouse_company_name                = models.CharField(max_length = 100, blank = True, null = True, verbose_name = "Company Name")
    spouse_office_address              = models.CharField(max_length = 500, blank = True, null = True, verbose_name = "Office Address")
    spouse_company_web_address         = models.CharField(max_length = 100, blank = True, null = True, verbose_name = "Company Website Address")
    spouse_nature_of_business          = models.CharField(max_length = 100, blank = True, null = True, verbose_name = "Nature of Business")
    spouse_job_title                   = models.CharField(max_length = 50, blank = True, null = True, verbose_name = "Job Title")
    spouse_company_position            = models.CharField(choices = company_position_choices, max_length = 20, blank = True, null = True, verbose_name = "Company Position")
    spouse_job_length_of_stay_years    = models.IntegerField(blank = True, null = True, verbose_name = "Length of Stay (Years)")
    spouse_job_length_of_stay_months   = models.IntegerField(blank = True, null = True, verbose_name = "Length of Stay (Months)")
    spouse_office_phone_no             = models.CharField(max_length = 50, blank = True, null = True, verbose_name = "Office Phone / Fax Number")

    # If in business or in practice of profession,
    spouse_business_name                   = models.CharField(max_length = 100, blank = True, null = True, verbose_name = "Business Name")
    spouse_business_address                = models.CharField(max_length = 500, blank = True, null = True, verbose_name = "Business Address")
    spouse_business_web_address            = models.CharField(max_length = 100, blank = True, null = True, verbose_name = "Business Website Address")
    spouse_nature_of_business_work         = models.CharField(max_length = 50, blank = True, null = True, verbose_name = "Nature of Business / Work")
    spouse_job_length_of_operation_years   = models.IntegerField(blank = True, null = True, verbose_name = "Length of Operation (Years)")
    spouse_job_length_of_operation_months  = models.IntegerField(blank = True, null = True, verbose_name = "Length of Operation (Months)")

    spouse_name_prevemployer_business      = models.CharField(max_length = 100, blank = True, null = True, verbose_name = "Name of Previous Employer / Business")

    # If OFW,
    spouse_country_of_destination          = models.CharField(max_length = 100, blank = True, null = True, verbose_name = "Country of Destination")
    spouse_employment_base                 = models.CharField(choices = employment_base_choices, max_length = 5, blank = True, null = True, verbose_name = "Employment Base")

    # Statement of Income and Expenses

    borrower_monthly_income         = models.IntegerField(verbose_name = "Borrower's Gross Monthly Income")
    spouse_monthly_income           = models.IntegerField(verbose_name = "Spouse's Gross Monthly Income")
    borrower_monthly_expenses       = models.IntegerField(verbose_name = "Borrower's Gross Monthly Expenses")
    spouse_monthly_expenses         = models.IntegerField(verbose_name = "Spouse's Gross Monthly Expenses")

    # Statement of Assets and Liabilities
    # No verbose name yet

    # Assets
    cash_hand_with_banks_details    = models.CharField(max_length = 200)
    cash_hand_with_banks_amount     = models.IntegerField()
    real_estate_property_details    = models.CharField(max_length = 200)
    real_estate_property_amount     = models.IntegerField()
    motor_vehicle_details           = models.CharField(max_length = 200)
    motor_vehicle_amount            = models.IntegerField()

    # Liabilities
    ## Loans
    personal_salary_loan_bank                   = models.CharField(max_length = 100)
    personal_salary_loan_amortization           = models.IntegerField()
    personal_salary_loan_outstanding_balance    = models.IntegerField()
    car_loan_bank                               = models.CharField(max_length = 100)
    car_loan_amortization                       = models.IntegerField()
    car_loan_outstanding_balance                = models.IntegerField()
    housing_loan_bank                           = models.CharField(max_length = 100)
    housing_loan_amortization                   = models.IntegerField()
    housing_loan_outstanding_balance            = models.IntegerField()

    ## Credit Card

    card1_company               = models.CharField(max_length = 50, blank = True, null = True, verbose_name = "Company of Credit Card 1")
    card1_number                = models.CharField(max_length = 20, blank = True, null = True, verbose_name = "Credit Card 1 Number")
    card1_expiry_date           = models.CharField(max_length = 10, blank = True, null = True, verbose_name = "Credit Card 1 Expiry Date")
    card1_credit_limit          = models.IntegerField(blank = True, null = True, verbose_name = "Credit Card 1 Credit Limit")
    card1_outstanding_balance   = models.IntegerField(blank = True, null = True, verbose_name = "Credit Card 1 Outstanding Balance")

    card2_company               = models.CharField(max_length = 50, blank = True, null = True,verbose_name = "Company of Credit Card 2")
    card2_number                = models.CharField(max_length = 20, blank = True, null = True,verbose_name = "Credit Card 2 Number")
    card2_expiry_date           = models.CharField(max_length = 10, blank = True, null = True,verbose_name = "Credit Card 2 Expiry Date")
    card2_credit_limit          = models.IntegerField(blank = True, null = True, verbose_name = "Credit Card 2 Credit Limit")
    card2_outstanding_balance   = models.IntegerField(blank = True, null = True, verbose_name = "Credit Card 2 Outstanding Balance")

    # Others
    source_product_info_choices = [
        ('TV / Radio', 'TV / Radio'),
        ('Website', 'Website'),
        ('Flyer / Poster / Streamer', 'Flyer / Poster / Streamer'),
        ('Newspaper / Magazine', 'Newspaper / Magazine'),
        ('Direct Mail', 'Direct Mail'),
        ('UPBank Personnel', 'UPBank Personnel'),
        ('UPBank Client', 'UPBank Client'),
        ('Agency', 'Agency'),
        ('Others', 'Others')
    ]

    source_product_info    = models.CharField(max_length = 40, blank = True, null = True, verbose_name = "Source of Product Information")
    relative_working       = models.BooleanField(verbose_name = "Do you have relative working in UPBank?")
    relative_name          = models.CharField(max_length = 100, blank = True, null = True, verbose_name = "If yes, please state their name")

class PersonalReferences(models.Model):
    personal_reference_id       = models.AutoField(primary_key = True)
    account_number              = models.ForeignKey(User, on_delete=models.CASCADE)

    reference_name              = models.CharField(max_length = 200)
    reference_address           = models.CharField(max_length = 500)
    reference_contact_number    = models.CharField(max_length = 20)

class CreditBankReferences(models.Model):
    credit_bank_reference_id   = models.AutoField(primary_key = True)
    account_number              = models.ForeignKey(User, on_delete=models.CASCADE)

    bank_name                  = models.CharField(max_length = 100, verbose_name = "Name")
    bank_type                  = models.CharField(max_length = 100, verbose_name = "Type")
    bank_account_no            = models.CharField(max_length = 100, verbose_name = "Account Number")
    bank_monthly_amortization  = models.IntegerField(verbose_name = "Monthly Amortization")
    bank_maturity_date         = models.DateField(verbose_name = "Maturity Date")

class LoanApplication(models.Model):
    # Create a 9-digit unique reference number
    def create_unique_number():
        not_unique = True
        while not_unique:
            unique_ref = random.randint(100000000, 999999999)
            if not LoanApplication.objects.filter(loan_account_no=unique_ref):
                not_unique = False
        return str(unique_ref)

    loan_account_no = models.AutoField(primary_key = True)
    account_no      = models.ForeignKey(User, db_column = "id", on_delete = models.PROTECT)
    loan_account_ref_no = models.CharField(max_length=8, blank=True, editable=False, unique=True, null=True, default=create_unique_number)

    def __str__(self):
        return self.loan_account_ref_no

    application_status_choices = [
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
        ('For Review', 'For Review')
    ]
    
    application_status = models.CharField(choices = application_status_choices, max_length = 15, default="For Review")


    # Vehicle Information

    vehicle_type_choices = [
        ('Brand New', 'Brand New'),
        ('Used', 'Used'),
        ('Reconditioned', 'Reconditioned')
    ]
    
    loan_type_choices = [
        ('Personal', 'Personal'),
        ('Business', 'Business'),
        ('Public Use', 'Public Use'),
        ('Others', 'Others')
    ]

    loan_type           = models.CharField(choices = loan_type_choices, max_length = 15, verbose_name = "Purpose of Loan")

    date_of_application = models.DateField(auto_now_add = True)
    dealer              = models.CharField(max_length = 100)
    sales_agent         = models.CharField(max_length = 100)
    branch              = models.CharField(max_length = 100)
    car_brand           = models.CharField(max_length = 50)
    car_model           = models.CharField(max_length = 50)
    year_model          = models.IntegerField()
    vehicle_type        = models.CharField(choices = vehicle_type_choices, max_length = 15, verbose_name = "Type of Vehicle")
    rejection_reason    = models.CharField(max_length=400, blank = True, null = True)

class Loan(models.Model):
    loan_account_no         = models.OneToOneField(LoanApplication, on_delete = models.CASCADE, primary_key = True)

    loan_tag_choices = [
        ('Completed', 'Completed'),
        ('Delinquent', 'Delinquent'),
        ('In Loan Default', 'In Loan Default'),
        ('Ongoing', 'Ongoing')
    ]
    
    loan_tag                = models.CharField(choices = loan_tag_choices, max_length = 20, default = "Ongoing")

    total_term_choices = [
        (12, '12 Months'),
        (18, '18 Months'),
        (24, '24 Months'),
        (36, '36 Months'),
        (48, '48 Months'),
        (60, '60 Months')
    ]

    selling_prize           = models.DecimalField(max_digits=10, decimal_places=2, verbose_name = "Selling Price")
    downpayment_percent     = models.PositiveSmallIntegerField(validators=[MinValueValidator(20), MaxValueValidator(100)], verbose_name="Downpayment (in percent)")
    downpayment             = models.DecimalField(max_digits=10, decimal_places=2)
    total_term              = models.IntegerField(choices=total_term_choices, verbose_name="Payment Term")
    term_remaining          = models.IntegerField()
    amount_financed         = models.DecimalField(max_digits=10, decimal_places=2)
    aor                     = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Add-on Rate (AOR)") #already in percent
    monthly_amortization    = models.DecimalField(max_digits=10, decimal_places=2)
    months_missed_counter   = models.IntegerField(default = 0)
    next_pay_date           = models.DateTimeField(null = True, blank = True)
    last_pay_date           = models.DateTimeField(null = True, blank = True)

class OTCPayment(models.Model):
    otc_payment_id      = models.AutoField(primary_key=True)

    loan_account_ref_no = models.ForeignKey(LoanApplication, db_column="loan_account_ref_no", on_delete=models.PROTECT)
    transaction_date    = models.DateField()
    amount_paid         = models.DecimalField(max_digits = 11, decimal_places = 2)











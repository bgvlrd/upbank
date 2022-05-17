# Generated by Django 4.0.4 on 2022-05-17 09:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LoanApplication',
            fields=[
                ('loan_account_no', models.AutoField(primary_key=True, serialize=False)),
                ('application_status', models.CharField(choices=[('Approved', 'Approved'), ('Denied', 'Denied'), ('For Review', 'For Review')], default='For Review', max_length=15)),
                ('loan_type', models.CharField(choices=[('Personal', 'Personal'), ('Business', 'Business'), ('Public Use', 'Public Use'), ('Others', 'Others')], max_length=15, verbose_name='Purpose of Loan')),
                ('date_of_application', models.DateField(auto_now_add=True)),
                ('dealer', models.CharField(max_length=100)),
                ('sales_agent', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
                ('car_brand', models.CharField(max_length=50)),
                ('car_model', models.CharField(max_length=50)),
                ('year_model', models.IntegerField()),
                ('vehicle_type', models.CharField(choices=[('Brand New', 'Brand New'), ('Used', 'Used'), ('Reconditioned', 'Reconditioned')], max_length=15, verbose_name='Type of Vehicle')),
                ('account_no', models.ForeignKey(db_column='id', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalReferences',
            fields=[
                ('personal_reference_id', models.AutoField(primary_key=True, serialize=False)),
                ('reference_name', models.CharField(max_length=200)),
                ('reference_address', models.CharField(max_length=500)),
                ('reference_contact_number', models.CharField(max_length=20)),
                ('account_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OTCPayment',
            fields=[
                ('otc_payment_id', models.AutoField(primary_key=True, serialize=False)),
                ('transaction_date', models.DateField()),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=11)),
                ('loan_account_no', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='App.loanapplication')),
            ],
        ),
        migrations.CreateModel(
            name='LoanerInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('nationality', models.CharField(max_length=50)),
                ('residency', models.CharField(blank=True, choices=[('Resident', 'Resident'), ('Non-Resident', 'Non-Resident')], max_length=15, null=True)),
                ('birthdate', models.DateField()),
                ('birthplace', models.CharField(max_length=50)),
                ('educational_attainment', models.CharField(blank=True, choices=[('Elementary', 'Elementary'), ('High School', 'High School'), ('Vocational', 'Vocational'), ('Undergraduate', 'Undergraduate'), ('College', 'College'), ('Postgraduate', 'Postgraduate')], max_length=15, null=True)),
                ('civil_status', models.CharField(blank=True, choices=[('Single', 'Single'), ('Married', 'Married'), ('Legally Separated', 'Legally Separated'), ('Widow/Widower', 'Widow/Widower')], max_length=20, null=True)),
                ('tin', models.CharField(max_length=10, verbose_name='Tax Identification Number (TIN)')),
                ('sss_gsis_no', models.CharField(blank=True, max_length=20, null=True, verbose_name='SSS / GSIS Number')),
                ('present_address', models.CharField(max_length=500)),
                ('prev_address', models.CharField(max_length=500, verbose_name='Previous Address')),
                ('home_ownership', models.CharField(blank=True, choices=[('Owned', 'Owned'), ('Mortgaged', 'Mortgaged'), ('Rented', 'Rented'), ('Living with Parents/Relatives', 'Living with Parents/Relatives')], max_length=30, null=True)),
                ('length_of_stay_years', models.IntegerField(blank=True, null=True, verbose_name='Length of Stay (Years)')),
                ('length_of_stay_months', models.IntegerField(blank=True, null=True, verbose_name='Length of Stay (Months)')),
                ('telephone_no', models.CharField(max_length=20, verbose_name='Residential Telephone Number')),
                ('cellphone_no', models.CharField(max_length=15, verbose_name='Cellphone Number')),
                ('email_address', models.EmailField(max_length=254)),
                ('source_of_income', models.CharField(choices=[('Locally Employed - Private', 'Locally Employed - Private'), ('Locally Employed - Government', 'Locally Employed - Government'), ('Locally Employed - Self-employed', 'Locally Employed - Self-employed'), ('OFW Immigrant - Private', 'OFW Immigrant - Private'), ('OFW Immigrant - Government', 'OFW Immigrant - Government'), ('OFW Immigrant - Self-employed', 'OFW Immigrant - Self-employed'), ('OFW Non-Immigrant - Private', 'OFW Non-Immigrant - Private'), ('OFW Non-Immigrant - Government', 'OFW Non-Immigrant - Government'), ('OFW Non-Immigrant - Self-employed', 'OFW Non-Immigrant - Self-employed'), ('Unemployed - Remittance/Allottee', 'Unemployed - Remittance/Allottee'), ('Unemployed - Pension/Retired', 'Unemployed - Pension/Retired'), ('Unemployed - Student', 'Unemployed - Student'), ('Others', 'Others')], max_length=50)),
                ('status_of_employment', models.CharField(blank=True, choices=[('Permanent', 'Permanent'), ('Probationary', 'Probationary'), ('Contractual', 'Contractual')], max_length=15, null=True)),
                ('company_name', models.CharField(blank=True, max_length=100, null=True)),
                ('office_address', models.CharField(blank=True, max_length=500, null=True)),
                ('company_web_address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Company Website Address')),
                ('nature_of_business', models.CharField(blank=True, max_length=100, null=True)),
                ('job_title', models.CharField(blank=True, max_length=50, null=True)),
                ('company_position', models.CharField(blank=True, choices=[('Non-Officer', 'Non-Officer'), ('Jr. Officer', 'Jr. Officer'), ('Supervisor', 'Supervisor'), ('Middle Manager', 'Middle Manager'), ('Sr. Officer', 'Sr. Officer')], max_length=20, null=True)),
                ('job_length_of_stay_years', models.IntegerField(blank=True, null=True, verbose_name='Length of Stay (Years)')),
                ('job_length_of_stay_months', models.IntegerField(blank=True, null=True, verbose_name='Length of Stay (Months)')),
                ('office_phone_no', models.CharField(blank=True, max_length=50, null=True, verbose_name='Office Phone / Fax Number')),
                ('business_name', models.CharField(blank=True, max_length=100, null=True)),
                ('business_address', models.CharField(blank=True, max_length=500, null=True)),
                ('business_web_address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Business Website Address')),
                ('nature_of_business_work', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nature of Business / Work')),
                ('job_length_of_operation_years', models.IntegerField(blank=True, null=True, verbose_name='Length of Operation (Years)')),
                ('job_length_of_operation_months', models.IntegerField(blank=True, null=True, verbose_name='Length of Operation (Months)')),
                ('name_prevemployer_business', models.CharField(blank=True, max_length=100, null=True, verbose_name='Name of Previous Employer / Business')),
                ('country_of_destination', models.CharField(blank=True, max_length=100, null=True)),
                ('employment_base', models.CharField(blank=True, choices=[('Land', 'Land'), ('Sea', 'Sea'), ('Air', 'Air')], max_length=5, null=True)),
                ('dependent1_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Name')),
                ('dependent1_school', models.CharField(blank=True, max_length=100, null=True, verbose_name='School')),
                ('dependent1_age', models.IntegerField(blank=True, null=True, verbose_name='Age')),
                ('dependent1_level', models.CharField(blank=True, max_length=100, null=True, verbose_name='Level')),
                ('dependent1_type_of_school', models.CharField(blank=True, choices=[('Public', 'Public'), ('Exclusive', 'Exclusive'), ('Private Coed', 'Private Coed')], max_length=15, null=True, verbose_name='Type of School')),
                ('dependent2_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Name')),
                ('dependent2_school', models.CharField(blank=True, max_length=100, null=True, verbose_name='School')),
                ('dependent2_age', models.IntegerField(blank=True, null=True, verbose_name='Age')),
                ('dependent2_level', models.CharField(blank=True, max_length=100, null=True, verbose_name='Level')),
                ('dependent2_type_of_school', models.CharField(blank=True, choices=[('Public', 'Public'), ('Exclusive', 'Exclusive'), ('Private Coed', 'Private Coed')], max_length=15, null=True, verbose_name='Type of School')),
                ('spouse_full_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Full Name')),
                ('spouse_gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10, null=True, verbose_name='Gender')),
                ('spouse_nationality', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nationality')),
                ('spouse_residency', models.CharField(blank=True, choices=[('Resident', 'Resident'), ('Non-Resident', 'Non-Resident')], max_length=15, null=True, verbose_name='Residency')),
                ('spouse_birthdate', models.DateField(blank=True, null=True, verbose_name='Birthdate')),
                ('spouse_birthplace', models.CharField(blank=True, max_length=50, null=True, verbose_name='Birthplace')),
                ('spouse_educational_attainment', models.CharField(blank=True, choices=[('Elementary', 'Elementary'), ('High School', 'High School'), ('Vocational', 'Vocational'), ('Undergraduate', 'Undergraduate'), ('College', 'College'), ('Postgraduate', 'Postgraduate')], max_length=15, null=True, verbose_name='Educational Attainment')),
                ('spouse_civil_status', models.CharField(blank=True, choices=[('Single', 'Single'), ('Married', 'Married'), ('Legally Separated', 'Legally Separated'), ('Widow/Widower', 'Widow/Widower')], max_length=20, null=True, verbose_name='Civil Status')),
                ('spouse_tin', models.CharField(blank=True, max_length=10, null=True, verbose_name='Tax Identification Number (TIN)')),
                ('spouse_sss_gsis_no', models.CharField(blank=True, max_length=20, null=True, verbose_name='SSS / GSIS Number')),
                ('spouse_source_of_income', models.CharField(blank=True, choices=[('Locally Employed - Private', 'Locally Employed - Private'), ('Locally Employed - Government', 'Locally Employed - Government'), ('Locally Employed - Self-employed', 'Locally Employed - Self-employed'), ('OFW Immigrant - Private', 'OFW Immigrant - Private'), ('OFW Immigrant - Government', 'OFW Immigrant - Government'), ('OFW Immigrant - Self-employed', 'OFW Immigrant - Self-employed'), ('OFW Non-Immigrant - Private', 'OFW Non-Immigrant - Private'), ('OFW Non-Immigrant - Government', 'OFW Non-Immigrant - Government'), ('OFW Non-Immigrant - Self-employed', 'OFW Non-Immigrant - Self-employed'), ('Unemployed - Remittance/Allottee', 'Unemployed - Remittance/Allottee'), ('Unemployed - Pension/Retired', 'Unemployed - Pension/Retired'), ('Unemployed - Student', 'Unemployed - Student'), ('Others', 'Others')], max_length=50, null=True, verbose_name='Source of Income')),
                ('spouse_status_of_employment', models.CharField(blank=True, choices=[('Permanent', 'Permanent'), ('Probationary', 'Probationary'), ('Contractual', 'Contractual')], max_length=15, null=True, verbose_name='Status of Employment')),
                ('spouse_company_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Company Name')),
                ('spouse_office_address', models.CharField(blank=True, max_length=500, null=True, verbose_name='Office Address')),
                ('spouse_company_web_address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Company Website Address')),
                ('spouse_nature_of_business', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nature of Business')),
                ('spouse_job_title', models.CharField(blank=True, max_length=50, null=True, verbose_name='Job Title')),
                ('spouse_company_position', models.CharField(blank=True, choices=[('Non-Officer', 'Non-Officer'), ('Jr. Officer', 'Jr. Officer'), ('Supervisor', 'Supervisor'), ('Middle Manager', 'Middle Manager'), ('Sr. Officer', 'Sr. Officer')], max_length=20, null=True, verbose_name='Company Position')),
                ('spouse_job_length_of_stay_years', models.IntegerField(blank=True, null=True, verbose_name='Length of Stay (Years)')),
                ('spouse_job_length_of_stay_months', models.IntegerField(blank=True, null=True, verbose_name='Length of Stay (Months)')),
                ('spouse_office_phone_no', models.CharField(blank=True, max_length=50, null=True, verbose_name='Office Phone / Fax Number')),
                ('spouse_business_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Business Name')),
                ('spouse_business_address', models.CharField(blank=True, max_length=500, null=True, verbose_name='Business Address')),
                ('spouse_business_web_address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Business Website Address')),
                ('spouse_nature_of_business_work', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nature of Business / Work')),
                ('spouse_job_length_of_operation_years', models.IntegerField(blank=True, null=True, verbose_name='Length of Operation (Years)')),
                ('spouse_job_length_of_operation_months', models.IntegerField(blank=True, null=True, verbose_name='Length of Operation (Months)')),
                ('spouse_name_prevemployer_business', models.CharField(blank=True, max_length=100, null=True, verbose_name='Name of Previous Employer / Business')),
                ('spouse_country_of_destination', models.CharField(blank=True, max_length=100, null=True, verbose_name='Country of Destination')),
                ('spouse_employment_base', models.CharField(blank=True, choices=[('Land', 'Land'), ('Sea', 'Sea'), ('Air', 'Air')], max_length=5, null=True, verbose_name='Employment Base')),
                ('borrower_monthly_income', models.IntegerField(verbose_name="Borrower's Gross Monthly Income")),
                ('spouse_monthly_income', models.IntegerField(verbose_name="Spouse's Gross Monthly Income")),
                ('borrower_monthly_expenses', models.IntegerField(verbose_name="Borrower's Gross Monthly Expenses")),
                ('spouse_monthly_expenses', models.IntegerField(verbose_name="Spouse's Gross Monthly Expenses")),
                ('cash_hand_with_banks_details', models.CharField(max_length=200)),
                ('cash_hand_with_banks_amount', models.IntegerField()),
                ('real_estate_property_details', models.CharField(max_length=200)),
                ('real_estate_property_amount', models.IntegerField()),
                ('motor_vehicle_details', models.CharField(max_length=200)),
                ('motor_vehicle_amount', models.IntegerField()),
                ('personal_salary_loan_bank', models.CharField(max_length=100)),
                ('personal_salary_loan_amortization', models.IntegerField()),
                ('personal_salary_loan_outstanding_balance', models.IntegerField()),
                ('car_loan_bank', models.CharField(max_length=100)),
                ('car_loan_amortization', models.IntegerField()),
                ('car_loan_outstanding_balance', models.IntegerField()),
                ('housing_loan_bank', models.CharField(max_length=100)),
                ('housing_loan_amortization', models.IntegerField()),
                ('housing_loan_outstanding_balance', models.IntegerField()),
                ('card1_company', models.CharField(max_length=50)),
                ('card1_number', models.CharField(max_length=20)),
                ('card1_expiry_date', models.CharField(max_length=10)),
                ('card1_credit_limit', models.IntegerField()),
                ('card1_outstanding_balance', models.IntegerField()),
                ('card2_company', models.CharField(max_length=50)),
                ('card2_number', models.CharField(max_length=20)),
                ('card2_expiry_date', models.CharField(max_length=10)),
                ('card2_credit_limit', models.IntegerField()),
                ('card2_outstanding_balance', models.IntegerField()),
                ('source_product_info', models.CharField(blank=True, choices=[('Locally Employed - Private', 'Locally Employed - Private'), ('Locally Employed - Government', 'Locally Employed - Government'), ('Locally Employed - Self-employed', 'Locally Employed - Self-employed'), ('OFW Immigrant - Private', 'OFW Immigrant - Private'), ('OFW Immigrant - Government', 'OFW Immigrant - Government'), ('OFW Immigrant - Self-employed', 'OFW Immigrant - Self-employed'), ('OFW Non-Immigrant - Private', 'OFW Non-Immigrant - Private'), ('OFW Non-Immigrant - Government', 'OFW Non-Immigrant - Government'), ('OFW Non-Immigrant - Self-employed', 'OFW Non-Immigrant - Self-employed'), ('Unemployed - Remittance/Allottee', 'Unemployed - Remittance/Allottee'), ('Unemployed - Pension/Retired', 'Unemployed - Pension/Retired'), ('Unemployed - Student', 'Unemployed - Student'), ('Others', 'Others')], max_length=40, null=True, verbose_name='Source of Product Information')),
                ('relative_working', models.BooleanField(verbose_name='Do you have relative working in UPBank?')),
                ('relative_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='If yes, please state')),
                ('account_number', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_tag', models.CharField(choices=[('Completed', 'Completed'), ('Delinquent', 'Delinquent'), ('In Loan Default', 'In Loan Default')], max_length=20)),
                ('selling_prize', models.DecimalField(decimal_places=2, max_digits=10)),
                ('downpayment', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_term', models.IntegerField()),
                ('term_remaining', models.IntegerField()),
                ('amount_financed', models.DecimalField(decimal_places=2, max_digits=10)),
                ('aor', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Add-on Rate (AOR)')),
                ('monthly_amortization', models.DecimalField(decimal_places=2, max_digits=10)),
                ('months_missed_counter', models.IntegerField(default=0)),
                ('loan_account_no', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='App.loanapplication')),
            ],
        ),
        migrations.CreateModel(
            name='CreditBankReferences',
            fields=[
                ('credit_bank_reference_id', models.AutoField(primary_key=True, serialize=False)),
                ('bank_name', models.CharField(max_length=100, verbose_name='Name')),
                ('bank_type', models.CharField(max_length=100, verbose_name='Type')),
                ('bank_account_no', models.CharField(max_length=100, verbose_name='Account Number')),
                ('bank_monthly_amortization', models.IntegerField(verbose_name='Monthly Amortization')),
                ('bank_maturity_date', models.DateField(verbose_name='Maturity Date')),
                ('account_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.DecimalField(decimal_places=2, max_digits=11)),
                ('bank_status', models.CharField(choices=[('Active', 'Active'), ('Closed', 'Closed')], max_length=10)),
                ('account_number', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

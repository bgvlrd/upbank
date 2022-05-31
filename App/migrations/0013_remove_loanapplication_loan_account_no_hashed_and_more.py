# Generated by Django 4.0.4 on 2022-05-30 15:40

import App.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0012_remove_otcpayment_loan_account_no_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loanapplication',
            name='loan_account_no_hashed',
        ),
        migrations.RemoveField(
            model_name='otcpayment',
            name='loan_account_no_hashed',
        ),
        migrations.AddField(
            model_name='loanapplication',
            name='loan_account_ref_no',
            field=models.CharField(blank=True, default=App.models.LoanApplication.create_unique_number, editable=False, max_length=8, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='otcpayment',
            name='loan_account_ref_no',
            field=models.ForeignKey(db_column='loan_account_ref_no', default=1, on_delete=django.db.models.deletion.PROTECT, to='App.loanapplication'),
            preserve_default=False,
        ),
    ]

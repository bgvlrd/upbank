# Generated by Django 4.0.4 on 2022-05-20 13:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App', '0002_alter_loanerinformation_card1_company_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bankaccount',
            name='id',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='id',
        ),
        migrations.AlterField(
            model_name='bankaccount',
            name='account_number',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='loan',
            name='loan_account_no',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='App.loanapplication'),
        ),
        migrations.AlterField(
            model_name='loan',
            name='loan_tag',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Delinquent', 'Delinquent'), ('In Loan Default', 'In Loan Default')], default='Completed', max_length=20),
        ),
    ]

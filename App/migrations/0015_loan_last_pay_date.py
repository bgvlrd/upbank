# Generated by Django 4.0.4 on 2022-06-03 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0014_loan_next_pay_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='last_pay_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

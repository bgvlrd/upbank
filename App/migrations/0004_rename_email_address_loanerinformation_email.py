# Generated by Django 4.0.4 on 2022-05-28 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_remove_bankaccount_id_remove_loan_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loanerinformation',
            old_name='email_address',
            new_name='email',
        ),
    ]

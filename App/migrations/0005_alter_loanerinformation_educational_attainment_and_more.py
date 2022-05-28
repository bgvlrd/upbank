# Generated by Django 4.0.4 on 2022-05-28 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_rename_email_address_loanerinformation_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanerinformation',
            name='educational_attainment',
            field=models.CharField(blank=True, choices=[('Elementary', 'Elementary'), ('High School', 'High School'), ('Vocational', 'Vocational'), ('College Studies', 'College Studies'), ('College (Undergraduate Degree)', 'College (Undergraduate Degree)'), ('College (Postgraduate Degree)', 'College (Postgraduate Degree)')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='loanerinformation',
            name='spouse_educational_attainment',
            field=models.CharField(blank=True, choices=[('Elementary', 'Elementary'), ('High School', 'High School'), ('Vocational', 'Vocational'), ('College Studies', 'College Studies'), ('College (Undergraduate Degree)', 'College (Undergraduate Degree)'), ('College (Postgraduate Degree)', 'College (Postgraduate Degree)')], max_length=30, null=True, verbose_name='Educational Attainment'),
        ),
    ]

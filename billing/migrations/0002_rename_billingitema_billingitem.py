# Generated by Django 3.2.4 on 2021-08-07 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BillingItema',
            new_name='BillingItem',
        ),
    ]

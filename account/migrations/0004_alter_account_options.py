# Generated by Django 4.0.4 on 2022-04-22 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_account_balance'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'ordering': ['-created_at'], 'verbose_name': 'Account', 'verbose_name_plural': 'Accounts'},
        ),
    ]
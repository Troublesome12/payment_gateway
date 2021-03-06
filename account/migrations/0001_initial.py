# Generated by Django 4.0.4 on 2022-04-21 19:00

import django.contrib.postgres.indexes
from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('holder_name', models.CharField(blank=True, max_length=200, null=True)),
                ('account_no', models.CharField(max_length=16)),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=15)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Account',
                'verbose_name_plural': 'Accounts',
            },
        ),
        migrations.AddIndex(
            model_name='account',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['id'], name='account_acc_id_cb8b0c_brin'),
        ),
        migrations.AddIndex(
            model_name='account',
            index=models.Index(fields=['id', 'is_active'], name='account_acc_id_3e0cbe_idx'),
        ),
        migrations.AddIndex(
            model_name='account',
            index=models.Index(fields=['id', 'email'], name='account_acc_id_2bae65_idx'),
        ),
        migrations.AddIndex(
            model_name='account',
            index=models.Index(fields=['holder_name', 'account_no', 'balance'], name='account_acc_holder__80c2bc_idx'),
        ),
    ]

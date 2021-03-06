# Generated by Django 4.0.4 on 2022-04-21 19:00

import django.contrib.postgres.indexes
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('from_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_from_account', to='account.account')),
                ('to_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_to_account', to='account.account')),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payments',
            },
        ),
        migrations.AddIndex(
            model_name='payment',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['id'], name='payment_pay_id_de44d0_brin'),
        ),
        migrations.AddIndex(
            model_name='payment',
            index=models.Index(fields=['from_account', 'to_account', 'amount'], name='payment_pay_from_ac_6882fa_idx'),
        ),
    ]

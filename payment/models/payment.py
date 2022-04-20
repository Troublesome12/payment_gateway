from django.db import models

import uuid
from django.contrib.postgres.indexes import BrinIndex
from django.utils import timezone

from account.models import Account


class PaymentManager(models.Manager):
    def make_payment(self, req_data):
        return self.create(**req_data)

    def get_payments(self):
        return self.all()


class Payment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    from_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='payment_from_account')
    to_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='payment_to_account')
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    objects = PaymentManager()

    class Meta:
        indexes = [
            BrinIndex(fields=['id']),
            models.Index(
                fields=[
                    'from_account',
                    'to_account',
                    'amount',
                ]
            ),
        ]

        verbose_name = "Payment"
        verbose_name_plural = "Payments"

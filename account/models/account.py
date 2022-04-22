from django.db import models

import uuid
from django.contrib.postgres.indexes import BrinIndex
from django.utils import timezone


class AccountManager(models.Manager):
    def create_account(self, req_data):
        return self.create(**req_data)

    def get_accounts(self):
        return self.filter(is_active=True).values('id', 'holder_name', 'email', 'account_no', 'balance')

    def get_account_by_id(self, account_id):
        return self.filter(pk=account_id, is_active=True).last()

    def get_account_by_no(self, account_no):
        return self.filter(account_no=account_no, is_active=True).last()

    def account_exists(self, account_no):
        if self.filter(account_no=account_no, is_active=True).count():
            return True
        return False

    def email_exists(self, email):
        if self.filter(email=email, is_active=True).count():
            return True
        return False

    def update_account(self, account_id, **req_data):
        self.filter(pk=account_id).update(**req_data)
        return self.filter(pk=account_id).last()

    def delete_account(self, account_id):
        return self.filter(pk=account_id).update(is_active=False)

    def update_balance(self, account_id, balance):
        self.filter(pk=account_id).update(balance=balance)
        return self.filter(pk=account_id).last()


class Account(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    holder_name = models.CharField(max_length=200, blank=True, null=True)
    account_no = models.CharField(max_length=16)
    email = models.EmailField(max_length=255, blank=True, null=True)
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=200.00)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    objects = AccountManager()

    class Meta:
        indexes = [
            BrinIndex(fields=['id']),
            models.Index(fields=['id', 'is_active']),
            models.Index(fields=['id', 'email']),
            models.Index(
                fields=[
                    'holder_name',
                    'account_no',
                    'balance',
                ]
            ),
        ]

        ordering = ['-created_at']

        verbose_name = "Account"
        verbose_name_plural = "Accounts"

    def __str__(self):
        return f'{self.holder_name} - {self.account_no}'

# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'from_account',
        'to_account',
        'amount',
        'created_at',
        'updated_at',
    )
    list_filter = ('from_account', 'to_account', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'

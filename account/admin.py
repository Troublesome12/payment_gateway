# -*- coding: utf-8 -*-              
from django.contrib import admin

from .models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'holder_name',
        'account_no',
        'email',
        'balance',
        'is_active',
        'created_at',
        'updated_at',
    )
    list_filter = ('is_active', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'

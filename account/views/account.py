from django.shortcuts import render
from django.views.generic import ListView
from django.views import View

from account.models import Account
from payment.models import Payment


class AccountListView(ListView):
    """
    @URL: /accounts/
    """

    model = Account
    template_name = 'account_list.html'
    context_object_name = 'accounts'
    ordering = ['-created_at']


class AccountPaymentListView(View):
    """
    @URL: /accounts/payments/752a8253-a599-4e09-95c6-b4257f5c2892/
    """

    def get(self, request, account_id, *args, **kwargs):
        debit_payments = Payment.objects.get_debits(account_id)
        credit_payments = Payment.objects.get_credits(account_id)
        context = {"debits": debit_payments, "credits": credit_payments}
        return render(request, 'account_payment_list.html', context)

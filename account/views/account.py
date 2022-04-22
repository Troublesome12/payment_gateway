from http.client import HTTPResponse

from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.views import View
from django.contrib import messages

from account.forms import AccountForm
from account.models import Account
from payment.models import Payment


class AccountListView(ListView):
    """
    @URL: /accounts/
    """

    model = Account
    template_name = 'account_list.html'
    context_object_name = 'accounts'

    def get_queryset(self):
        return Account.objects.get_accounts()


class AccountCreateView(CreateView):
    """
    @URL: /accounts/create/
    """

    def get(self, request, *args, **kwargs):
        form = AccountForm(None)
        return render(request, 'account_create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form_data = AccountForm(request.POST)
        if not form_data.is_valid():
            return render(request, "account_create.html", {'form': form_data})

        try:
            form_data.save()
            messages.success(request, 'Account creation successful')
            return redirect('/accounts/')

        except Exception as ex:
            print(ex)
            messages.error(request, 'Account creation failed')
        return redirect('/accounts/')


class AccountPaymentListView(View):
    """
    @URL: /accounts/payments/752a8253-a599-4e09-95c6-b4257f5c2892/
    """

    def get(self, request, account_id):
        try:
            debit_payments = Payment.objects.get_debits(account_id)
            credit_payments = Payment.objects.get_credits(account_id)
            context = {"debits": debit_payments, "credits": credit_payments}
            return render(request, 'account_payment_list.html', context)

        except Exception as ex:
            print(ex)

        return render(request, 'account_list.html')

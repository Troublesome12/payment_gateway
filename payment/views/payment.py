from django.shortcuts import render, redirect
from django.views.generic import CreateView

from account.models import Account
from payment.forms import PaymentForm
from django.db import transaction

class MakePaymentView(CreateView):
    """
    @URL: /payments/
    """

    def get(self, request, *args, **kwargs):
        form = PaymentForm(None)
        return render(request, 'make_payment.html', {'form': form})

    def __update_balance(self, payment):
        receiver_balance = float(payment.to_account.balance) + float(payment.amount)
        sender_balance = float(payment.from_account.balance) - float(payment.amount)
        Account.objects.update_balance(payment.from_account.id, sender_balance)
        Account.objects.update_balance(payment.to_account.id, receiver_balance)

    def post(self, request, *args, **kwargs):
        details = PaymentForm(request.POST)
        if details.is_valid():
            payment = details.save(commit=False)

            with transaction.atomic():
                self.__update_balance(payment)
                payment.save()

            return redirect('/accounts/')

        return render(request, "make_payment.html", {'form': details})

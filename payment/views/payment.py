from django.shortcuts import render, redirect
from django.views.generic import CreateView
from payment.forms import PaymentForm
from django.db import transaction

class MakePaymentView (CreateView):
    """
    @URL: /payments/
    """

    def get(self, request, *args, **kwargs):
        form = PaymentForm(None)
        return render(request, 'make_payment.html', {'form': form})

    def post(self, request, *args, **kwargs):
        details = PaymentForm(request.POST)
        if details.is_valid():
            payment = details.save(commit=False)
            print(payment.to_account.balance)
            with transaction.atomic():
                payment.to_account.balance = payment.to_account.balance + payment.amount
                payment.from_account.balance = payment.from_account.balance - payment.amount
                payment.save()

            return redirect('/accounts/')

        return render(request, "make_payment.html", {'form': details})

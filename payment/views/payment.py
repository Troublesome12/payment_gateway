from django.shortcuts import render
from django.views.generic import ListView

from account.models import Account


class MakePayment(ListView):
    """
    @URL: /accounts/
    """

    def get(self, request):
        context = {'navbar': 'make_payment'}
        return render(request, 'make_payment.html', context)

from django.shortcuts import render
from django.views.generic import ListView

from account.models import Account


class GetAccountList(ListView):
    """
    @URL: /accounts/
    """
    def get(self, request):
        try:
            accounts = Account.objects.get_accounts()
            context = {'accounts': accounts}
            return render(request, 'accounts.html', context)

        except Exception as e:
            print(e)
        return render(request, 'accounts.html')


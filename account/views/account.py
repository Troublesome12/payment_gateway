from django.views.generic import ListView

from account.models import Account


class AccountListView(ListView):
    """
    @URL: /accounts/
    """

    model = Account
    template_name = 'account_list.html'
    context_object_name = 'accounts'
    ordering = ['-created_at']

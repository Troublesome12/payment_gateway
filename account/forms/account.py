from django.forms import ModelForm

from account.models import Account
from applibs.util import is_name_valid, is_account_valid


class AccountForm(ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['holder_name'].required = True

	class Meta:
		model = Account
		fields = ["holder_name", "account_no", "email"]

	def clean(self):
		super(AccountForm, self).clean()

		holder_name = self.cleaned_data.get('holder_name')
		account_no = self.cleaned_data.get('account_no')
		email = self.cleaned_data.get('email')

		# Validating Holder Name
		if not is_name_valid(holder_name):
			self._errors['holder_name'] = self.error_class(['It\'s not a valid name'])

		# Validating Account No
		if not is_account_valid(account_no):
			self._errors['account_no'] = self.error_class(['Account no must have 16 digit numeric values'])

		if Account.objects.account_exists(account_no):
			self._errors['account_no'] = self.error_class(['Account no already exists'])

		# Validating Email Address
		if Account.objects.email_exists(email):
			self._errors['email'] = self.error_class(['Email address already exists'])

		return self.cleaned_data

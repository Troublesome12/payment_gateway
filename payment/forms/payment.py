from django.forms import ModelForm
from payment.models import Payment


class PaymentForm(ModelForm):
	class Meta:
		model = Payment
		fields = ["from_account", "to_account", "amount"]

	def clean(self):
		super(PaymentForm, self).clean()

		from_account = self.cleaned_data.get('from_account')
		to_account = self.cleaned_data.get('to_account')
		amount = self.cleaned_data.get('amount')

		if amount > from_account.balance:
			self._errors['from_account'] = self.error_class(['Sender does\'t have enough balance to make this payment'])

		if amount <= 0:
			self._errors['amount'] = self.error_class(['Amount must be a positive value'])

		if from_account == to_account:
			self._errors['from_account'] = self.error_class(['Sender and Receiver can\'t be same'])
			self._errors['to_account'] = self.error_class(['Sender and Receiver can\'t be same'])

		if not from_account.is_active:
			self._errors['from_account'] = self.error_class(['Sender has been blocked'])

		if not to_account.is_active:
			self._errors['to_account'] = self.error_class(['Receiver has been blocked'])

		return self.cleaned_data

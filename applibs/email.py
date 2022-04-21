from django.conf import settings
from django.core.mail import send_mail


def send_receiver_email(receiver_account, sender_account, amount):
	subject = 'Payment Received'
	message = (
		f'Hi {receiver_account.holder_name}, £{amount} is received to your account {receiver_account.account_no} from {sender_account.account_no}.',
		f"Your current balance is £{receiver_account.balance}"
	)

	email_from = settings.EMAIL_HOST_USER
	recipient_list = [receiver_account.email, ]
	send_mail(subject, message, email_from, recipient_list)

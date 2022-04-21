from django.conf import settings
from django.core.mail import send_mail


def send_receiver_email(receiver_account, sender_account, amount):
	subject = 'Payment Received'
	body = (
		f'Hi {receiver_account.holder_name}, £{amount} is received to your account {receiver_account.account_no} from {sender_account.account_no}.'
		f"Your current balance is £{receiver_account.balance}"
	)

	from_email = settings.EMAIL_HOST_USER
	recipient_list = [receiver_account.email, ]
	send_mail(subject, body, from_email, recipient_list)


def send_sender_email(receiver_account, sender_account, amount):
	subject = 'Payment Sent'
	body = (
		f'Hi {sender_account.holder_name}, £{amount} is sent from your account {sender_account.account_no} to {receiver_account.account_no}.' 
		f"Your current balance is £{sender_account.balance}"
	)

	from_email = settings.EMAIL_HOST_USER
	recipient_list = [sender_account.email, ]
	send_mail(subject, body, from_email, recipient_list)

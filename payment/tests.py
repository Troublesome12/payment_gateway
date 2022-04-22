from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from faker import Faker

from account.models import Account
from applibs.util import generate_random_account_no


class PaymentViewTest(TestCase):
    def setUp(self):
        number_of_accounts = 2
        fake = Faker()
        for account_id in range(number_of_accounts):
            Account.objects.create(
                holder_name=fake.name(),
                account_no=generate_random_account_no(),
                email=f'{fake.unique.first_name()}@gmail.com'
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/payments/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('make-payment'))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_sender_balance_decrease(self):
        amount = 25.25
        accounts = Account.objects.all()
        sender = accounts[0]
        receiver = accounts[1]
        data = {
            "from_account": sender.id,
            "to_account": receiver.id,
            "amount": amount
        }
        sender_balance_before_payment = sender.balance
        response = self.client.post(reverse('make-payment'), data, follow=True)
        self.assertEqual(response.status_code, HTTPStatus.OK)

        accounts = Account.objects.all()
        sender = accounts[0]

        sender_balance_after_payment = sender.balance
        self.assertEqual(float(sender_balance_before_payment - sender_balance_after_payment), float(amount))

    def test_receiver_balance_increase(self):
        amount = 15.15
        accounts = Account.objects.all()
        sender = accounts[0]
        receiver = accounts[1]
        data = {
            "from_account": sender.id,
            "to_account": receiver.id,
            "amount": amount
        }
        receiver_balance_before_payment = receiver.balance
        response = self.client.post(reverse('make-payment'), data, follow=True)
        self.assertEqual(response.status_code, HTTPStatus.OK)

        accounts = Account.objects.all()
        receiver = accounts[1]

        receiver_balance_after_payment = receiver.balance

        self.assertEqual(float(receiver_balance_after_payment - receiver_balance_before_payment), float(amount))

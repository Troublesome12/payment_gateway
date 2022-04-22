from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from faker import Faker

from account.models import Account
from applibs.util import generate_random_account_no


class AccountViewTest(TestCase):
    fake = Faker()

    def setUp(self):
        number_of_accounts = 20
        for account_id in range(number_of_accounts):
            Account.objects.create(
                holder_name=self.fake.name(),
                account_no=generate_random_account_no(),
                email=f'{self.fake.unique.first_name()}@gmail.com'
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/accounts/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

        response = self.client.get('/accounts/create/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

        response = self.client.get('/accounts/payments/123456/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('account-list'))
        self.assertEqual(response.status_code, HTTPStatus.OK)

        response = self.client.get(reverse('account-create'))
        self.assertEqual(response.status_code, HTTPStatus.OK)

        response = self.client.get(reverse('account-payment-list', kwargs={'account_id': "1234"}))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('account-list'))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'account_list.html')

        response = self.client.get(reverse('account-create'))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'account_create.html')

    def test_lists_all_accounts(self):
        response = self.client.get(reverse('account-list'))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == False)
        self.assertEqual(len(response.context['accounts']), 20)

    def test_account_soft_delete(self):
        response = self.client.get(reverse('account-list'))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(len(response.context['accounts']), 20)

        # Now soft delete 10 accounts
        accounts = Account.objects.all()[:10]

        for account in accounts:
            account.is_active = False
            account.save()

        response = self.client.get(reverse('account-list'))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(len(response.context['accounts']), 10)

    def test_account_creation(self):
        data = {
            "holder_name": self.fake.name(),
            "account_no": generate_random_account_no(),
            "email": f'{self.fake.unique.first_name()}@gmail.com'
        }
        response = self.client.post(reverse('account-create'), data, follow=True)
        self.assertEqual(response.status_code, HTTPStatus.OK)

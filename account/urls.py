"""merchant_ops URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URL conf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from account.views import AccountListView, AccountCreateView, AccountPaymentListView

urlpatterns = [
    path('', AccountListView.as_view(), name="account-list"),
    path('create/', AccountCreateView.as_view(), name="account-create"),
    path('payments/<str:account_id>/', AccountPaymentListView.as_view(), name="account-payment-list"),
]

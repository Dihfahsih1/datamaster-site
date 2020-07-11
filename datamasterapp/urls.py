from django.conf.urls import url, include
from django.urls import path
from datamasterapp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^online-estimates-and-quotations', views.estimates_quotations, name='estimates-quotations'),
    url(r'^online-invoicing-and-billing', views.invoicing_billing, name='invoicing-billing'),
    url(r'^expenses-management', views.expenses_purchases, name='expenses-management'),
    url(r'^simple-online-accounting', views.accounting_reporting, name='accounting-reporting'),
    url(r'^feedback', views.feedback, name='feedback'),
    
]
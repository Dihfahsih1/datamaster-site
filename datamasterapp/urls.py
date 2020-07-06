from django.conf.urls import url
from django.urls import path
from datamasterapp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^online-estimates-and-quotations', views.estimates_quotations, name='estimates-quotations'),
]
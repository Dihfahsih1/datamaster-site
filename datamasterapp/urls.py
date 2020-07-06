from django.conf.urls import url
from django.urls import path
from datamasterapp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^Feature', views.feature_details, name='feature_details'),
]
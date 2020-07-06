from django.shortcuts import render
from.models import *
def index(request):
	features = Feature.objects.all()
	reasons = Reason.objects.all()
	context={'features':features,'reasons':reasons}
	return render(request, 'home.html', context)
def estimates_quotations(request):
	details=FeatureDetail.objects.filter(Feature__Feature_Title='Estimates & Quotations')
	for i in details:
		sub_title=(i.Feature.Feature_Sub_Title)
		description=(i.Feature.Feature_Description)
	context={'details':details,'sub':sub_title,'description':description}
	return render(request, 'feature_details.html', context)

def invoicing_billing(request):
	details=FeatureDetail.objects.filter(Feature__Feature_Title='Invoicing & Billing')
	context={'details':details}
	return render(request, 'feature_details.html', context)

def expenses_purchases(request):
	details=FeatureDetail.objects.filter(Feature__Feature_Title='Expenses & Purchases')
	context={'details':details}
	return render(request, 'feature_details.html', context)

def accounting_reporting(request):
	details=FeatureDetail.objects.filter(Feature__Feature_Title='Accounting & Reporting')
	context={'details':details}
	return render(request, 'feature_details.html', context)
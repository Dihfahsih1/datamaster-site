from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from.models import *
from.forms import *
from django.core.mail import EmailMessage

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
		demo=(i.Feature.Feature_Image)
	context={'details':details,'sub':sub_title,'description':description,'demo':demo}
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

def feedback(request):
    if request.method=="POST":
        form=FeedbackForm(request.POST, request.FILES,)
        if form.is_valid():
            company_email = CompanyDetail.objects.get(id=1)
            emailing_to=company_email.email_address
            client_name= form.cleaned_data.get('full_name')
            mail_subject = form.cleaned_data.get('subject')   
            message =  form.cleaned_data.get('comment')  
            received_from = form.cleaned_data.get('email') 
            email = EmailMessage( to=[emailing_to],
                subject=mail_subject, body=message,
                from_email=[received_from ], reply_to=[received_from]
            )  
            email.send()
            messages.success(request, f'Your Feedback has been sent successfully')
            return redirect('index')
    else:
        form=FeedbackForm()
        return render(request, 'feedback_form.html',{'form':form})
    return render(request, 'feedback_form.html')   
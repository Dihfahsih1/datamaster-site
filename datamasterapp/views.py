from django.shortcuts import render
from.models import *
def index(request):
	features = Feature.objects.all()
	reasons = Reason.objects.all()
	context={'features':features,'reasons':reasons}
	return render(request, 'home.html', context)
def feature_details(request):
	details=FeatureDetail.objects.all()
	context={'details':details}
	return render(request, 'feature_detaill.html', context)

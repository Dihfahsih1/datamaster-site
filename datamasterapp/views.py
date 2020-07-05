from django.shortcuts import render
from.models import *
def index(request):
	features = Features.objects.all()
	context={'features':features}
	return render(request, 'home.html', context)

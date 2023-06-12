from django.http import HttpResponse

def index(request):
	return HttpResponse('Hey, World!!!')

def designs(request):
	return HttpResponse('<h2>DESIGN</h2>')
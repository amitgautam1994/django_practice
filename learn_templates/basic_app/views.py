from django.shortcuts import render

# Create your views here.

def base(request):
	return render(request, 'basic_app/basic_app.html')

def index(request):
	dict1={'text':'hello world', 'num':100}
	return render(request, 'basic_app/index.html',dict1)

def other(request):
	return render(request, 'basic_app/other.html')

def relative(request):
	return render(request, 'basic_app/rel_url.html')
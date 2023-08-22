from django.shortcuts import render

# Create your views here.



def home(request):


	return render(request, 'base/home.html')



def about(request):

	return render(request, 'base/about.html')


def resume(request):

	return render(request, 'base/resume.html')


def portfolio(request):

	return render(request, 'base/portfolio.html')


def academics(request):

	return render(request, 'base/academics.html')



def rugby(request):

	return render(request, 'base/rugby.html')



def contact(request):

	return render(request, 'base/contact.html')
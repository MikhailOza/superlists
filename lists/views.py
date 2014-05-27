from django.shortcuts import render
from django.http import HttpResponse


#Create Views here

def home_page(request):
	return render(request, 'home.html')
	

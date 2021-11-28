from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	"""This function creates the index for the organizer app.
	"""
	return HttpResponse("Hello, friendo. You're at the organizer index.")
from django.shortcuts import render
from django.http import HttpResponse
# Create my views here.

def index(request):
    return HttpResponse("Hello mysite index page.")


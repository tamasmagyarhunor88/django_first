from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at them polls index.")

def hunor(request):
    return HttpResponse("Magyar-Hunor Tamas £1000 per day, Porsche incoming")


from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def yummy(request):
    return HttpResponse("<h1>swiggy food </h1>")


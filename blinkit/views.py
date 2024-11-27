from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def blinkit(request):
    return HttpResponse("<h1>Blinkit delivered to you in 10 minutes.</h1>")


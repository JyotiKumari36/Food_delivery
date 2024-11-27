from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def magicpin(request):
    return HttpResponse("<h1>magicpin food </h1>")


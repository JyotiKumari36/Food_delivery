from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def magicpin(request):
    return HttpResponse("<h1> Some time offer given by magicpin app</h1>")


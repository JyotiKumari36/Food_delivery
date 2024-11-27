from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def yummy(request):
    return HttpResponse("<h1><marquee direction=right>Tendency to evoke feelings of hunger</marquee></h1>")


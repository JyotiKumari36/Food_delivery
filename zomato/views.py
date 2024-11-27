from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse

def spicy(request):
    return HttpResponse("<h1>Zomato food is hurry up for deliver</h1>")

from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse

def spicy(request):
    return HttpResponse("<h1>Zomato delivers fast compared to swiggy</h1>
                         <p>the founder of zomato is Deepinder Goyal</p>")

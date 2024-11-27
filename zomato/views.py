from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse

def spicy(request):
    return HttpResponse('''<h1><marquee>Zomato delivers fast compared to swiggy</marquee></h1>
    <p>The founder of zomato is Deepinder Goyal</p>''')

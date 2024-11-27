from zomato.views import *
from django.urls import path

urlpatterns=[
    path('spicy/',spicy,name='spicy')
]
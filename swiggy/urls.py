from swiggy.views import *
from django.urls import path

urlpatterns=[
    path('yummy/',yummy,name='yummy'),
]
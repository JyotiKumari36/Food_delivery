"""
URL configuration for food_delicious project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin


from django.urls import path, include
import zomato,swiggy

from blinkit.views import * 
from magicpin.views import * 

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('zomato/',include('zomato.urls')),
    path('swiggy/',include('swiggy.urls')),
    

    path('magicpin/',magicpin,name='magicpin.urls'),
    path('blinkit/',blinkit,name='blinkit'),
   
]

from django.urls import path
from .views import *
urlpatterns = [
    path('', app, name = "Homepage."),
    path('0/', app0, name = "Ano0the0r pa0ge"),
    ]
    

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def test_mango(request):
    return HttpResponse("<h1>I am Mango<h1/>")
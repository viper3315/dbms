from django.shortcuts import render
from django.http import HttpResponse

from products.models import Product

def index(request):

    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def purchase(request):
    return render(request, 'pages/purchase.html')

def thankyou(request):
    return render(request, 'pages/thankyou.html')

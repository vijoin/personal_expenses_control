from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.all()
    return render(request, "products/index.html", context={'products': products})

def new(request):
    return render(request, 'products/new.html', {})
from django.shortcuts import render
from .models import Product
from .forms import ProductForm


def index(request):
    products = Product.objects.all()
    return render(request, "products/index.html", context={'products': products})

def new(request):
    form = ProductForm()
    return render(request, 'products/new.html', {'form': form})
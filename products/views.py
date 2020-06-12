from django.shortcuts import render
from .models import Product
from expenses.models import ProductExpense


def index(request):
    products = Product.objects.all()
    return render(request, "products/index.html", context={'products': products})

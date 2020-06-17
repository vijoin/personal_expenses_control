from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm


def index(request):
    products = Product.objects.all()
    return render(request, "products/index.html", context={'products': products})


def new(request, product_id=None):
    if product_id:
        product = Product.objects.get(pk=product_id)
        form = ProductForm(instance=product)
    else:
        form = ProductForm()

    if request.method == 'POST':
        if product_id:
            form = ProductForm(request.POST, request.FILES, instance=product)
        else:
            form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save()
            return redirect('products-edit', product_id=product.id)

    return render(request, 'products/new.html', {'form': form})

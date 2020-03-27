from django.shortcuts import render


def index(request):
    print("PRODUCTS")
    return render(request, "products/index.html", context={})

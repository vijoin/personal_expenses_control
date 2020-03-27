from django.contrib import admin
from .models import Product, ProductBrand, ProductModel, ProductUom, ProductCategory

admin.site.register(Product)
admin.site.register(ProductBrand)
admin.site.register(ProductModel)
admin.site.register(ProductUom)
admin.site.register(ProductCategory)


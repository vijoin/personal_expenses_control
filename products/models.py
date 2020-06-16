from django.db import models


class ProductBrand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ProductModel(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ProductUom(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE)
    model = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    uom = models.ForeignKey(ProductUom, on_delete=models.CASCADE)
    category = models.ManyToManyField(ProductCategory)
    image = models.ImageField(null=True)
    #ToDo picture
    # ToDo max: Maximum price paid for this product (taken from expenses details)
    # ToDo min: Minimum price paid for this product (taken from expenses details)
    # ToDo last: Last price paid for this product (taken from expenses details)

    def __str__(self):
        return f"{self.name} ({self.uom.symbol})"

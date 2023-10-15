from django.db import models
from django.utils import timezone

# Supplier Model
class Supplier(models.Model):
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=10)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.name}"

# Product Model
class Product(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

# Purchase Model
class Purchase(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, default='')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_type = models.CharField(max_length=100,)
    color = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=100)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.product}"

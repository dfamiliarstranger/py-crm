from django.db import models, IntegrityError
from django.db.models import Sum
from django.utils import timezone
from django.db.models import F

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
    
#Inventory Item
class InventoryItem(models.Model):
    id = models.AutoField(primary_key=True)
    size = models.CharField(max_length=100, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_type = models.CharField(max_length=100, blank=True)
    color = models.CharField(max_length=100, blank=True)
    quantity = models.IntegerField(default=0)  # Default quantity is set to 0

    def __str__(self):
        return f"{self.product} - {self.size} - {self.color} - {self.product_type}"

# Purchase Model
class Purchase(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,)
    product_type = models.CharField(max_length=100, blank=True)
    color = models.CharField(max_length=100, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(null=True)
    size = models.IntegerField(null=True, blank=True)
    unit = models.CharField(max_length=100, blank=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.product}"

    

# def update_inventory():
#     purchases = Purchase.objects.all()

#     for purchase in purchases:
#         inventory_item, created = InventoryItem.objects.get_or_create(
#             product=purchase.product,
#             color=purchase.color,
#             product_type=purchase.product_type,
#             size=purchase.size,
#             defaults={'quantity': 0}  # Set a default value for quantity
#         )

#         # Update quantity using F() expression if the item already exists
#         if not created:
#             inventory_item.quantity = F('quantity') + purchase.quantity
#             inventory_item.save()

def update_inventory():
    purchases = Purchase.objects.all()

    for purchase in purchases:
        inventory_item, created = InventoryItem.objects.get_or_create(
            product=purchase.product,
            color=purchase.color,
            product_type=purchase.product_type,
            size=purchase.size,
            defaults={'quantity': 0}  # Set a default value for quantity
        )

        # Update quantity using F() expression if the item already exists
        if not created:
            # Use update to perform a database-level update using F()
            InventoryItem.objects.filter(
                pk=inventory_item.pk
            ).update(quantity=F('quantity') + purchase.quantity)

class Sales(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    inventory_item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)
    size = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.product} - {self.quantity} units at {self.price} each"
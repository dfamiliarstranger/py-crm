from django.db import models, IntegrityError
from django.db.models import Sum
from django.utils import timezone
from django.db.models import F
from django.db import transaction

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
    inventory_updated = models.BooleanField(default=False)  # Flag to track inventory updates


    def __str__(self):
        return f"{self.product}"

def update_inventory(purchase):
    try:
        with transaction.atomic():
            # Check if the item already exists in the inventory
            inventory_item = InventoryItem.objects.filter(
                product=purchase.product,
                color=purchase.color,
                product_type=purchase.product_type,
                size=purchase.size
            ).first()

            if inventory_item:
                # If the item exists, update its quantity
                inventory_item.quantity = F('quantity') + purchase.quantity
                inventory_item.save()
            else:
                # If the item doesn't exist, create a new inventory item
                InventoryItem.objects.create(
                    product=purchase.product,
                    color=purchase.color,
                    product_type=purchase.product_type,
                    size=purchase.size,
                    quantity=purchase.quantity
                )

            # Mark the purchase as inventory updated
            purchase.inventory_updated = True
            purchase.save()

            return True  # Successfully updated inventory
    except Exception as e:
        # Handle exceptions, log errors, and return False to indicate failure
        print(f"Error updating inventory: {str(e)}")
        return False
   

class Sales(models.Model):
    inventory_item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)
    size = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        product_name = self.inventory_item.product.name
        return f"{product_name} - {self.quantity} units at {self.price} each"
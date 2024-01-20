from django.contrib import admin
from .models import Supplier, Purchase, Product, Sales, InventoryItem

# Register your models here.

admin.site.register(Supplier)
admin.site.register(Purchase)
admin.site.register(Product)
admin.site.register(Sales)
admin.site.register(InventoryItem)


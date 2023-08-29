from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# # my Sample Model


# class Product(models.Model):
#     product_name = 
#     company =  #onetomany
#     created_at =
#     updated_at =

# # ShrinkWrapper Product
# class ShrinkWrapper(Product):
#     PRODUCT_TYPE_CHOICES = (
#         ('VRG', 'Virgin'),
#         ('PPR', 'Preprocessed'),
#     )
#     product_type = models.CharField(max_length=3, choices=PRODUCT_TYPE_CHOICES)
#     weight = models.DecimalField(max_digits=10, decimal_places=2)


# # Cap Product
# class Cap(Product):
#     CAP_SIZE_CHOICES = (
#         ('28mm', '28mm'),
#         ('30mm', '30mm'),
#     )
#     measurement_size = models.CharField(max_length=4, choices=CAP_SIZE_CHOICES)
#     quantity_per_bag = models.PositiveIntegerField()
#     color = models.CharField(max_length=64)
    


# # Product Model
# class Product(models.Model):
#     product_price = models.IntegerField()
#     product_selling_price = models.IntegerField()

#     def __str__(self):
#         return f"Product {self.id}"




# # # Preforms Product
# # class Preforms(Product):
# #     measurement_unit = models.CharField(max_length=20, default='units')
# #     quantity = models.PositiveIntegerField()
# #     color = models.CharField(max_length=64)
# #     units = models.PositiveBigIntegerField()

# Supplier Model
class Supplier(models.Model):
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=10)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
    
    

# # # Purchase Model
# # class Purchase(models.Model):
# #     content_type = models.ForeignKey(
# #         ContentType,
# #         on_delete=models.CASCADE,
# #         limit_choices_to={
# #             'model__in': ('product', 'shrinkwrapper', 'cap', 'preforms')
# #         }
# #     )
# #     object_id = models.PositiveIntegerField()
# #     product = GenericForeignKey('content_type', 'object_id')
# #     quantity = models.PositiveIntegerField()
# #     unit = models.CharField(max_length=20)
# #     amount = models.DecimalField(max_digits=10, decimal_places=2)
# #     unit_cost = models.DecimalField(max_digits=10, decimal_places=2)
# #     size = models.CharField(max_length=20, blank=True, null=True)
# #     color = models.CharField(max_length=20, blank=True, null=True)
# #     total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

# #     def __str__(self):
# #         return f"{self.product} - {self.quantity} {self.unit}"

# # # Customer Model
# # class Customer(models.Model):
# #     name = models.CharField(max_length=100)
# #     address = models.TextField()
# #     phone = models.CharField(max_length=20)
# #     email = models.EmailField(unique=True)

# #     def __str__(self):
# #         return self.name

    
# # # Sale Model
# # class Sale(models.Model):
# #     product = models.ForeignKey(Product, on_delete=models.CASCADE)
# #     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
# #     quantity = models.PositiveIntegerField()
# #     unit = models.CharField(max_length=20)
# #     amount = models.DecimalField(max_digits=10, decimal_places=2)
    
# #     def __str__(self):
# #         return f"{self.product} - {self.quantity} {self.unit} to {self.customer}"
# #     pass



# # # Store Model
# # class Store(models.Model):
# #     product = models.OneToOneField(Product, on_delete=models.CASCADE)
# #     quantity = models.PositiveIntegerField(default=0)

# #     def __str__(self):
# #         return f"{self.product.name} - {self.quantity} units"


    
    
from django.db import transaction
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse 
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from .models import Product, Supplier, Purchase, InventoryItem, update_inventory, Sales
from .forms import AddSupplierForm, ProductForm, PurchaseForm

# Create your views here.
#Login Views
def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, ('home.html'))
   


def login_user(request):
    # check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "you have been logged in!")
            return redirect('home')
        else:
            messages.success(request, ("invalid login credentials, Try again !!!"))
            return redirect('login')
    else:
        return render(request, 'login.html') 
    

def logout_user(request):
    if request.user.is_authenticated:
     messages.success(request, "You have logged out!!")
    return redirect('login')


#SUPPLIER CRUD OPERATIONS

def supplier(request):
    supplier = Supplier.objects.all()
    if request.user.is_authenticated:
        return render(request, 'supplier/supplier.html', {'suppliers': supplier})
    else:
        messages.success(request, ("You are not logged in!!"))
        return redirect('login')
    
def supplier_detail(request, pk):
    if request.user.is_authenticated:
        supplier_detail = get_object_or_404(Supplier, id=pk)
        return render(request, 'supplier/supplier_detail.html', {'supplier_detail': supplier_detail})
    else:
        messages.success(request, ("You are not logged in!!"))
        return redirect('login')
    
def delete_supplier(request, pk):
    if request.user.is_authenticated:
        delete_supplier = get_object_or_404(Supplier, id=pk)
        delete_supplier.delete()
        messages.success(request, ("Succesfully Deleted!!"))
        return redirect('supplier')
    else:
        messages.success(request, ("You are not logged in!!"))
        return redirect('login')

def add_supplier(request):
    form = AddSupplierForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_supplier = form.save()
                messages.success(request, ("Supplier Succesfully saved"))
                return redirect('supplier')
        return render (request, 'supplier/add_supplier.html', {'form': form})
    else:
        messages.success(request, ("You are not logged in!!"))
        return redirect('login')
    
def update_supplier(request, pk):
    if request.user.is_authenticated:
        current_supplier = get_object_or_404(Supplier, id=pk)
        form = AddSupplierForm(request.POST or None, instance=current_supplier)
        if form.is_valid():
            form.save()
            messages.success(request, ("Record Updated !!"))
            return redirect('supplier')
        return render (request, 'supplier/update_supplier.html', {'form': form})
    else:
        messages.success(request, ("You are not logged in!!"))
        return redirect('login')




#PRODUCTS-DETAILS

def product(request):
    product = Product.objects.all()
    if request.user.is_authenticated:
        return render(request, 'products/index.html', {'products': product})
    else:
        messages.success(request, ("You are not logged in!!"))
        return redirect('login')
    
def add_product(request):
    form = ProductForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_product = form.save()
                messages.success(request, ("Product Succesfully saved"))
                return redirect('product')
        return render (request, 'products/add_products.html', {'form': form})
    else:
        messages.success(request, ("You are not logged in!!"))
        return redirect('login')
    
def product_detail(request, pk):
    if request.user.is_authenticated:
        product_detail = get_object_or_404(Product, id=pk)
        return render(request, 'products/product_detail.html', {'product_detail': product_detail})
    else:
        messages.success(request, ("You are not logged in!!"))
        return redirect('login')
    
def update_product(request, pk):
    if request.user.is_authenticated:
        current_product = get_object_or_404(Product, id=pk)
        form = ProductForm(request.POST or None, instance=current_product)
        if form.is_valid():
            form.save()
            messages.success(request, ("Record Updated !!"))
            return redirect('product')
        return render (request, 'products/update_product.html', {'form': form})
    else:
        messages.success(request, ("You are not logged in!!"))
        return redirect('product')
    
def delete_product(request, pk):
    if request.user.is_authenticated:
        delete_product = get_object_or_404(Product, id=pk)
        delete_product.delete()
        messages.success(request, ("Succesfully Deleted!!"))
        return redirect('product')
    else:
        messages.success(request, ("You are not logged in!!"))
        return redirect('login')
    
#PURCHASES

def purchase(request):
    purchase = Purchase.objects.all()
    if request.user.is_authenticated:
        return render(request, 'purchases/index.html', {'purchases': purchase})
    else:
        messages.success(request, ("You are not logged in!!"))
        return redirect('login')
    
def add_purchase(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PurchaseForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Product successfully saved")
                return redirect('purchase')
        else:
            form = PurchaseForm()

        suppliers = Supplier.objects.all()
        products = Product.objects.all()
        selected_product = request.POST.get('product', '')  # Get the selected product from the form

        return render(request, 'purchases/add_purchase.html', {
            'form': form,
            'suppliers': suppliers,
            'products': products,
            'selected_product': selected_product,
        })
    else:
        messages.success(request, "You are not logged in!!")
        return redirect('login')
    

def preform_form(request):
    if request.method == 'POST':
        # Get the data from the form
        product_id = request.POST.get('product', None)
        supplier_id = request.POST.get('supplier', None)
        color = request.POST.get('color', '')
        product_type = request.POST.get('product_type', '')
        quantity = request.POST.get('quantity')
        size = request.POST.get('size', '')  # Default to empty string if not provided
        price = request.POST.get('price')
        
        # Validate product and supplier IDs
        if product_id is None or supplier_id is None:
            return HttpResponse("Product and Supplier are required fields.")
        
        try:
            product = Product.objects.get(id=product_id)
            supplier = Supplier.objects.get(id=supplier_id)
        except (Product.DoesNotExist, Supplier.DoesNotExist):
            return HttpResponse("Invalid Product or Supplier selected.")
        
        # Convert 'size' to a number if it's not an empty string
        if size:
            size = float(size)
        
        # Calculate the total
        total = float(quantity) * float(price)
        
        # Create a Purchase object and save it to the database
        purchase = Purchase(
            product=product,
            supplier=supplier,
            color=color,
            product_type=product_type,
            size=size,  # Will be an empty string if not provided
            price=price,
            quantity=quantity,
            total=total
        )
        purchase.save()
        
        return redirect('purchase')   # You can define a success_page URL in your urls.py
    else:
        # Handle GET requests or other cases as needed
        products = Product.objects.all()
        suppliers = Supplier.objects.all()
        return render(request, 'purchases/preform.html', {'products': products, 'suppliers': suppliers})

    
# def preform_form(request):
#     if request.method == 'POST':
#         # Get the data from the form
#         product_id = request.POST.get('product', None)
#         supplier_id = request.POST.get('supplier', None)
#         color = request.POST.get('color', '')
#         product_type = request.POST.get('product_type', '')
#         quantity = request.POST.get('quantity')
#         size = request.POST.get('size')
#         price = request.POST.get('price')
        
#         # Validate product and supplier IDs
#         if product_id is None or supplier_id is None:
#             return HttpResponse("Product and Supplier are required fields.")
        
#         try:
#             product = Product.objects.get(id=product_id)
#             supplier = Supplier.objects.get(id=supplier_id)
#         except (Product.DoesNotExist, Supplier.DoesNotExist):
#             return HttpResponse("Invalid Product or Supplier selected.")
        
#         # Calculate the total
#         total = float(quantity) * float(price)
        
#         # Create a Purchase object and save it to the database
#         purchase = Purchase(
#             product=product,
#             supplier=supplier,
#             color=color,
#             product_type=product_type,
#             size=size,
#             price=price,
#             quantity=quantity,
#             total=total
#         )
#         purchase.save()
        
#         return redirect('purchase')  # You can define a success_page URL in your urls.py
        
#     # If it's a GET request, render the form
#     products = Product.objects.all()
#     suppliers = Supplier.objects.all()
#     return render(request, 'purchases/preform.html', {'products': products, 'suppliers': suppliers})


def inventory_view(request):
    # Recalculate and update the inventory
    update_inventory()
    
    # Retrieve the inventory items
    inventory_items = InventoryItem.objects.all()

    # Pass the inventory items to the template context
    context = {'inventory_items': inventory_items}

    # Render the template with the context
    return render(request, 'inventory.html', context)



# def sales_view(request):
#     if request.method == 'POST':
#         product_id = request.POST.get('product')
#         color = request.POST.get('color')
#         product_type = request.POST.get('product_type')
#         quantity = int(request.POST.get('quantity'))
#         price = float(request.POST.get('price'))

#         try:
#             inventory_item = InventoryItem.objects.get(
#                 product_id=product_id,
#                 color=color,
#                 product_type=product_type,
#             )
#         except InventoryItem.DoesNotExist:
#             return render(request, 'sales/sales_form.html', {'error': "Product not found in the inventory. Please check your input."})

#         if inventory_item.quantity < quantity:
#             return render(request, 'sales/sales_form.html', {'error': "Not enough quantity available in the inventory."})

#         # Create a Sales object to record the sale
#         sale = Sales(
#             product=inventory_item.product,
#             inventory_item=inventory_item,
#             quantity=quantity,
#             price=price,
#         )
#         sale.save()

#         # Update the inventory after the sale
#         inventory_item.quantity -= quantity
#         inventory_item.save()

#         messages.success(request, "Sale recorded successfully.")
#         return redirect('sales')  # You can define a success page URL

#     inventory_items = InventoryItem.objects.all()
#     return render(request, 'sales/sales.html', {'inventory_items': inventory_items})

@transaction.atomic
def sales_view(request):
    if request.method == 'POST':
        product_id = request.POST.get('product')
        color = request.POST.get('color')
        product_type = request.POST.get('product_type')
        quantity = int(request.POST.get('quantity'))
        size_str = request.POST.get('size')
        size = int(size_str) if size_str.isdigit() else 0
        price = float(request.POST.get('price'))

        try:
            inventory_item = InventoryItem.objects.select_for_update().get(
                product_id=product_id,
                color=color,
                product_type=product_type,
                size = size
            )
        except InventoryItem.DoesNotExist:
            return render(request, 'sales/sales_form.html', {'error': "Product not found in the inventory. Please check your input."})

        if inventory_item.quantity < quantity:
            return render(request, 'sales/sales_form.html', {'error': "Not enough quantity available in the inventory."})

        # Create a Sales object to record the sale
        sale = Sales(
            product=inventory_item.product,
            inventory_item=inventory_item,
            quantity=quantity,
            size=size,
            price=price,
        )
        sale.save()

        # Update the inventory after the sale
        inventory_item.quantity -= quantity
        inventory_item.save()

        messages.success(request, "Sale recorded successfully.")
        return redirect('sales')  # You can define a success page URL

    inventory_items = InventoryItem.objects.all()
    return render(request, 'sales/sales_form.html', {'inventory_items': inventory_items})


def sales_history(request):
    sales = Sales.objects.all()
    return render(request, 'sales/sales.html', {'sales': sales})
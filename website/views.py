
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse 
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from .models import Product, Supplier, Purchase, InventoryItem, update_inventory, Sales
from .forms import AddSupplierForm, ProductForm
from django import forms
from django.core.exceptions import ValidationError
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
    
def add_purchases(request):
    if request.method == 'POST':
        product_id = request.POST.get('product', None)
        supplier_id = request.POST.get('supplier', None)
        color = request.POST.get('color', '')
        product_type = request.POST.get('product_type', '')
        quantity = request.POST.get('quantity')
        size = request.POST.get('size', '')  
        price = request.POST.get('price')
        
        if product_id is None or supplier_id is None:
            return HttpResponse("Product and Supplier are required fields.")
        
        try:
            product = Product.objects.get(id=product_id)
            supplier = Supplier.objects.get(id=supplier_id)
        except (Product.DoesNotExist, Supplier.DoesNotExist):
            return HttpResponse("Invalid Product or Supplier selected.")
        
        
        if size:
            size = float(size)
        
        total = float(quantity) * float(price)
        

        purchase = Purchase(
            product=product,
            supplier=supplier,
            color=color,
            product_type=product_type,
            size=size,  
            price=price,
            quantity=quantity,
            total=total
        )
        purchase.save()
        update_inventory(purchase)
        return redirect('purchase') 
    else:
        products = Product.objects.all()
        suppliers = Supplier.objects.all()
        return render(request, 'purchases/preform.html', {'products': products, 'suppliers': suppliers})


#SALES
def sales(request):
    sales = Sales.objects.all()
    if request.user.is_authenticated:
        return render(request, 'sales/sales.html', {'sales': sales})
    else:
        messages.success(request, ("You are not logged in!!"))
        return redirect('login')

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import InventoryItem, Sales

def record_sales(request):
    if request.method == 'POST':
        inventory_item_id = request.POST.get('inventory_item')
        quantity = int(request.POST.get('quantity'))
        price = float(request.POST.get('price'))

        # Check if the inventory item exists and if there is enough inventory
        try:
            inventory_item = InventoryItem.objects.get(id=inventory_item_id)
            if inventory_item.quantity < quantity:
                raise ValueError("Insufficient inventory for this sale.")
        except (InventoryItem.DoesNotExist, ValueError) as e:
            messages.error(request, str(e))
            return redirect('record_sales')

        try:
            # Deduct sold quantity from inventory
            inventory_item.quantity -= quantity
            inventory_item.save()

            # Create a sales record
            Sales.objects.create(
                inventory_item=inventory_item,
                quantity=quantity,
                price=price
            )

            messages.success(request, "Sale recorded successfully!")
            return redirect('sales')
        
        except Exception as e:
            messages.error(request, f"Failed to record sale: {str(e)}")
            return redirect('sales_form')
    else:
        # Fetch available inventory items for the dropdown
        available_items = InventoryItem.objects.filter(quantity__gt=0)
        return render(request, 'sales/sales_form.html', {'available_items': available_items})

    


# Inventory view
def inventory_view(request):
    if request.method == 'POST':
        update_inventory()
    inventory_items = InventoryItem.objects.all()
    context = {'inventory_items': inventory_items}

    # Render the template with the context
    return render(request, 'inventory.html', context)



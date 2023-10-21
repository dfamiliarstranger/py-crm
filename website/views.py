from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from .models import Product, Supplier, Purchase
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
     messages.success(request, ("You have logged out!!"))
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
    form = PurchaseForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_purchase = form.save()
                messages.success(request, ("Product Succesfully saved"))
                return redirect('purchase')
        return render (request, 'purchases/add_purchase.html', {'form': form})
    else:
        messages.success(request, ("You are not logged in!!"))
        return redirect('login')
    
def purchase_detail(request, pk):
    if request.user.is_authenticated:
        product_detail = get_object_or_404(Purchase, id=pk)
        return render(request, 'purchases/purchase_detail.html', {'purchase_detail': purchase_detail})
    else:
        messages.success(request, ("You are not logged in!!"))
        return redirect('login')
    

#Inventory

class InventoryListView(ListView):
    model = Purchase
    template_name = 'inventory/index.html'
    context_object_name = 'inventory'


# views.py


def add_item(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            # Save the form data
            form.save()
            return redirect('add_product')  # Redirect to a success page
    else:
        form = PurchaseForm()

    context = {'form': form}
    return render(request, 'purchases/add_item.html', context)
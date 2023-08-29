from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from .models import Supplier
from .forms import AddSupplierForm

# Create your views here.

def home(request):
    # records = Record.objects.all()
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, ('home.html'))
    # {'records':records}


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


def supplier(request):
    supplier = Supplier.objects.all()
    if request.user.is_authenticated:
        return render(request, 'supplier.html', {'suppliers': supplier})
    else:
        messages.success(request, ("You are not logged in!!"))
        return redirect('login')
    
def supplier_detail(request, pk):
    if request.user.is_authenticated:
        supplier_detail = get_object_or_404(Supplier, id=pk)
        return render(request, 'supplier_detail.html', {'supplier_detail': supplier_detail})
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
        return render (request, 'add_supplier.html', {'form': form})
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
        return render (request, 'update_supplier.html', {'form': form})
    else:
        messages.success(request, ("You are not logged in!!"))
        return redirect('login')
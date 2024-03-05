from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Supplier, Purchase, Product
from django import forms




class AddSupplierForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"supplier name", "class":"form-control"}), label="")
    code = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"supplier code", "class":"form-control"}), label="")
    address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"address", "class":"form-control"}), label="")
    phone = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"phone number", "class":"form-control"}), label="")
    email = forms.EmailField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"email", "class":"form-control"}), label="")
 
    class Meta:
        model = Supplier
        exclude = ("user", )


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name']


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = '__all__'

    def clean_size(self):
        size = self.cleaned_data['size']
        if size is not None and size != '':
            try:
                size = float(size)
                if size < 0:
                    raise forms.ValidationError("Size must be a non-negative number.")
            except ValueError:
                raise forms.ValidationError("Size must be a valid number.")
        else:
            size = None  # Set to None if empty or not provided
        return size


class TestProductForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['product', 'supplier', 'color', 'product_type', 'quantity', 'size', 'price', 'total']





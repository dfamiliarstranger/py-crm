from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Supplier

class AddSupplierForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"supplier name", "class":"form-control"}), label="")
    code = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"supplier code", "class":"form-control"}), label="")
    address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"address", "class":"form-control"}), label="")
    phone = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"phone number", "class":"form-control"}), label="")
    email = forms.EmailField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"email", "class":"form-control"}), label="")
 
    class Meta:
        model = Supplier
        exclude = ("user", )
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

    def __init__(self, *args, **kwargs):
        super(PurchaseForm, self).__init__(*args, **kwargs)

    #     # Create a dynamic choice field for the product_type based on available products
    #     product_choices = Product.objects.values_list('name', flat=True)
    #     self.fields['product_type'] = forms.ChoiceField(
    #         choices=[(choice, choice) for choice in product_choices],
    #         widget=forms.Select(attrs={'onchange': 'update_fields();'})
    #     )

    # def clean(self):
    #     cleaned_data = super().clean()
    #     product_type = cleaned_data.get('product_type')

    #     # If 'shrinkwrapper' is selected, make 'color' and 'quantity' fields null
    #     if product_type == 'shrinkwrapper':
    #         cleaned_data['color'] = None
    #         cleaned_data['quantity'] = None

    #     return cleaned_data






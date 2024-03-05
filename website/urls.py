from django.urls import path
from . import views


urlpatterns = [ 
        path('', views.login_user, name="login"),
        path('home', views.home, name="home"),
        path('logout', views.logout_user, name="logout"),

        path('supplier/', views.supplier, name="supplier"),
        path('supplier/<int:pk>', views.supplier_detail, name="supplier_detail"),
        path('delete_supplier/<int:pk>', views.delete_supplier, name="delete_supplier"), 
        path('add_supplier', views.add_supplier, name="add_supplier"), 
        path('update_supplier/<int:pk>', views.update_supplier, name="update_supplier"),

        path('product/', views.product, name="product"),
        path('add_product', views.add_product, name="add_product"), 
        path('product/<int:pk>', views.product_detail, name="product_detail"), 
        path('update_product/<int:pk>', views.update_product, name="update_product"),
        path('delete_product/<int:pk>', views.delete_product, name="delete_product"), 

        path('purchase/', views.purchase, name="purchase"),
        path('add_purchase/', views.add_purchases, name="add_purchases"),
        
        
        
        path('inventory/', views.inventory_view, name='inventory'),

        path('sales/', views.sales, name='sales'),
        path('sales_form/', views.record_sales, name='sales_form'),

        path('invoice/', views.invoice, name='invoice'),
        path('sales/<int:sales_id>/invoice/', views.generate_invoice, name='generate_invoice'),

    ]
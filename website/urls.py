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
    ]
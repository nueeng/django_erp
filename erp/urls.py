from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product_list', views.product_list, name='product_list'),
    path('product_create', views.product_create, name='product_create'),
    path('inbound_create', views.inbound_create, name='inbound_create'),
    path('outbound_create', views.outbound_create, name='outbound_create'),
    path('inventory', views.inventory, name='inventory'),
]
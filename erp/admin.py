from django.contrib import admin
from erp.models import Product, Inbound, Outbound, Inventory

# Register your models here.
admin.site.register(Product)
admin.site.register(Inbound)
admin.site.register(Outbound)
admin.site.register(Inventory)

from django.contrib import admin

# Register your models here.
from .models import InventoryItem
admin.site.register(InventoryItem)

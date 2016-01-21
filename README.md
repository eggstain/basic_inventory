This is a tool that was developed by an IT team so that they could keep track of their inventory in an inventory room.

It's a Django app

To install into your existing Django server:
Clone repo to "inventory" folder
Add 'inventory.apps.InventoryConfig', to INSTALLED_APPS in your project's setting.py
Add url(r'^inventory/', include('inventory.urls')), to urlpatterns in your project's urls.py
python manage.py makemigrations inventory && python manage.py migrate inventory

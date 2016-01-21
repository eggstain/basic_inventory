This is a tool that was developed by an IT so that they could keep track of their inventory in an inventory room.

It's a Django app

To install into your existing Django server:
Clone repo to "rba" folder
Add 'rba.apps.RbaConfig', to INSTALLED_APPS in your project's setting.py
Add url(r'^rba/', include('rba.urls')), to urlpatterns in your project's urls.py
python manage.py makemigrations rba python manage.py migrate rba

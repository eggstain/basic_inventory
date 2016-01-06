from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<inventoryitem_id>[0-9]+)/$', views.inventoryList, name='inventoryList'),
    url(r'^(?P<inventoryitem_id>[0-9]+)/change/$', views.change, name='change'),
    url(r'^scan/$', views.scan, name='scan'),
]

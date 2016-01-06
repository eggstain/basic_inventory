from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from .models import InventoryItem
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse

def index(request):
    inventory_list = InventoryItem.objects.order_by('-inventory_text')
    template = loader.get_template('inventory/index.html')
    context = {
        'inventory_list': inventory_list,
    }
    return HttpResponse(template.render(context, request))

def change(request, inventoryitem_id):
    stock_removed = 0
    stock_restored = 0
    item = get_object_or_404(InventoryItem, pk=inventoryitem_id)
    try:
        stock_removed = request.POST['removed']
    except (KeyError, InventoryItem.DoesNotExist):
        stock_removed = 0
    else:
        item.stock -= int(stock_removed)
        item.save()
        return HttpResponseRedirect(reverse('index', args=()))
    try:
        stock_restored = request.POST['added']
    except (KeyError, InventoryItem.DoesNotExist):
        stock_restored = 0
    else:
        item.stock += int(stock_restored)
        item.save()
        return HttpResponseRedirect(reverse('index', args=()))

def scan(request):
    try:
	barcode=request.POST['barcode']
	item = InventoryItem.objects.get(barcode=barcode)
	item.stock -= 1
        item.save()
    except:
        response = "Bad barcode"
	return HttpResponse(response)
    else:
        return HttpResponseRedirect(reverse('index', args=()))

def inventoryList(request, inventoryitem_id):
    response = "Here's the Help Desk Inventory %s"
    return HttpResponse(response % inventoryitem_id)

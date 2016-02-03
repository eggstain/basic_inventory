#Copyright 2015 Matthew Krohn
#
#This file is part of Basic Inventory.
#
#Basic Inventory is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""Definitions for various web page presentations"""

from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from .models import InventoryItem
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse

import smtplib
from email.mime.text import MIMEText

import settings

def index(request):
"""Generate list of items"""
    inventory_list = InventoryItem.objects.order_by('-inventory_text')
    template = loader.get_template('inventory/index.html')
    context = {
        'inventory_list': inventory_list,
    }
    return HttpResponse(template.render(context, request))

def check_low(item):
    if item.stock < item.minimum_stock:
        msg = MIMEText("We need more "+str(item.inventory_text)+\
            ". Stock should be "+str(item.minimum_stock)+\
            " but we only have "+str(item.stock))
        msg['Subject'] = "Low inventory notification"
        msg['From'] = settings.from_field
        msg['To'] = settings.to_address
        s = smtplib.SMTP(settings.smtp_server)
        s.sendmail(settings.from_address,settings.to_address,msg.as_string())
        s.quit

def change(request, inventoryitem_id):
"""Change in-stock value when requested at webpage"""
    stock_removed = 0
    stock_restored = 0
    item = get_object_or_404(InventoryItem, pk=inventoryitem_id)
    try:
	if request.POST['removed'] != "":
            stock_removed = request.POST['removed']
    except (KeyError, InventoryItem.DoesNotExist):
        stock_removed = 0
    else:
        item.stock -= int(stock_removed)
        item.save()
        check_low(item)
        return HttpResponseRedirect(reverse('index', args=()))
    try:
        if request.POST['added'] != "":
            stock_restored = request.POST['added']
    except (KeyError, InventoryItem.DoesNotExist):
        stock_restored = 0
    else:
        item.stock += int(stock_restored)
        item.save()
        return HttpResponseRedirect(reverse('index', args=()))

def scan(request):
"""If a barcode is scanned into the webpage, remove 1 from stock"""
    try:
	barcode=request.POST['barcode']
	item = InventoryItem.objects.get(barcode=barcode)
	item.stock -= 1
        item.save()
        check_low(item)
    except:
        response = "Bad barcode"
	return HttpResponse(response)
    else:
        return HttpResponseRedirect(reverse('index', args=()))

def inventory_list(request, inventoryitem_id):
"""Just a list of inventory"""
    response = "Here's the Help Desk Inventory %s"
    return HttpResponse(response % inventoryitem_id)

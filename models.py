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
"""Objects used by the program"""
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible  # only if you need to support Python 2
class InventoryItem(models.Model):
    """Any item that might be kept in stock"""
    inventory_text = models.CharField(max_length=200)
    barcode = models.CharField(max_length=50)
    restocking_link = models.CharField(max_length=200)
    stock = models.IntegerField(default=0)
    minimum_stock = models.IntegerField(default=0, null=True)
    def __str__(self):
        return self.inventory_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

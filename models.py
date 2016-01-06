from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible  # only if you need to support Python 2
class InventoryItem(models.Model):
    inventory_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    barcode = models.CharField(max_length=50)
    restocking_link = models.CharField(max_length=200)
    stock = models.IntegerField(default=0)
    def __str__(self):
        return self.inventory_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

from __future__ import unicode_literals
import moneyed
from djmoney.models.fields import MoneyField
from django.db import models

# Create your models here.

class Products(models.Model):
    product_name = models.CharField(max_length=50)
    product_description = models.TextField()
    weight = models.IntegerField()
    price = MoneyField(max_digits =10, decimal_places=2, default_currency='USD')
    cost = MoneyField(max_digits =10, decimal_places=2, default_currency='USD')
    category =models.CharField(max_length=50)


    


#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.db import models
from django.contrib import admin

# Create your models here.

class Product(models.Model):
    title=models.CharField(max_length=100,unique=True)
    description=models.TextField()
    image_url=models.URLField(max_length=200)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    date_available=models.DateField()

class Order(models.Model):
    name=models.CharField(max_length=50)
    address=models.TextField()
    email=models.EmailField()

class LineItem(models.Model):
    product=models.ForeignKey(Product)
    order=models.ForeignKey(Order)
    unit_price=models.DecimalField(max_digits=8,decimal_places=2)
    quantity=models.IntegerField()

class Cart(object):
    def __init__(self,*args,**kwargs):
        self.items=[]
        self.total_price=0

    def add_product(self,product):
        self.total_price+=product.price
        for item in self.items:
            if item.product.id==product.id:
                item.quantity+=1
                return
        self.items.append(LineItem(product=product,unit_price=product.price,quantity=1))

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','description','price')

admin.site.register(Product,ProductAdmin)
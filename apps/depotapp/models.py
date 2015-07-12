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

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','description','price')

admin.site.register(Product,ProductAdmin)
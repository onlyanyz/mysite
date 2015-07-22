from django.core.urlresolvers import reverse
from rest_framework.views import View
from rest_framework import serializers
from models import *

class LineItemResource(View):
    model=LineItem
    fields = ('product', 'unit_price', 'quantity')
    def product(self, instance):
        return instance.product.title
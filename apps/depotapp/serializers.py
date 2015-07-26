from rest_framework import serializers
from models import *

class LineItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=LineItem
        field=('product','unit_price','quantity')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        field=('title','description','image_url','price','date_available')
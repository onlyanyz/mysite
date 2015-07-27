from rest_framework import serializers
from models import *

class LineItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=LineItem
        field=('product','unit_price','quantity')

# class LineItemSerializer(serializers.Serializer):
#     def product(self,instance):
#         return instance.product.title
#     product=
#     unit_price=serializers.DecimalField(max_digits=8,decimal_places=2)
#     quantity=serializers.IntegerField()


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        field=('title','description','image_url','price','date_available')

# class ProductSerializer(serializers.Serializer):
#     title=serializers.CharField(max_length=100)
#     price=serializers.DecimalField(max_digits=8,decimal_places=2)

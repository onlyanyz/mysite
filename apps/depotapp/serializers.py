from rest_framework import serializers
from models import *

class LineItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=LineItem
        field=('product','unit_price','quantity')

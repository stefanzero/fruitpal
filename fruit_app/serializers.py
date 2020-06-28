from rest_framework import serializers
from .models import Commodity_Data


class CommodityDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commodity_Data
        fields = ('country', 'commodity', 'fixed_overhead', 'variable_cost')

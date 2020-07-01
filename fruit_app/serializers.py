from rest_framework import serializers
from .models import Commodity_Data, Country
from rest_framework import renderers
from django.core.serializers.json import DjangoJSONEncoder
import decimal
import uuid
from django.utils.functional import Promise


class CommodityDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commodity_Data
        fields = ('country', 'commodity', 'fixed_overhead', 'variable_cost')


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('country', 'name')


class MyJSONEncoder(DjangoJSONEncoder):
    def default(self, o):
        if isinstance(o, (decimal.Decimal, uuid.UUID, Promise)):
            return '{:.2f}'.format(o)
        else:
            return super().default(o)


class MyJSONRenderer(renderers.JSONRenderer):
    encoder_class = MyJSONEncoder


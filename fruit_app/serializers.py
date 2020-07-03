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
        fields = ('id', 'country', 'commodity', 'fixed_overhead', 'variable_cost')


class CountrySerializer(serializers.ModelSerializer):
    country_code = serializers.StringRelatedField(many=False)

    class Meta:
        model = Country
        fields = ('country_code', 'name')


class MyJSONEncoder(DjangoJSONEncoder):
    def default(self, o):
        if isinstance(o, (decimal.Decimal, uuid.UUID, Promise)):
            return '{:.2f}'.format(o)
        elif isinstance(o, Country):
            return Country.country_code
        else:
            return super().default(o)


class MyJSONRenderer(renderers.JSONRenderer):
    encoder_class = MyJSONEncoder


from django.test import TestCase
from ..models import Commodity_Data
from django.db.models import Q
import decimal


class Commodity_Data_Test(TestCase):
    """ Test module for Puppy model """

    def setUp(self):
        Commodity_Data.objects.create(
            country='MX',
            commodity='mango',
            fixed_overhead=decimal.Decimal(32.00),
            variable_cost=decimal.Decimal(1.24)
        )
        Commodity_Data.objects.create(
            country='BR',
            commodity='mango',
            fixed_overhead=decimal.Decimal(20.00),
            variable_cost=decimal.Decimal(1.42)
        )
        qs = Commodity_Data.objects.all()
        print('setUp')
        print(list(qs))

    def test_composite_key(self):
        qs = Commodity_Data.objects.filter(
            Q(country='MX') & Q(commodity='mango')
        )
        print(list(qs))
        count = qs.count()
        self.assertEqual(
            qs.count(), 1
        )

    def test_query_variable_cost(self):
        mango = Commodity_Data.objects.get(variable_cost=decimal.Decimal(1.24))
        print(mango)
        self.assertEqual(mango.country, 'MX')



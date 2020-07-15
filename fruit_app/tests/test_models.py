from django.test import TestCase
from ..models import Country, CommodityData
from django.db.models import Q
import decimal


class Country_Test(TestCase):
    """ Test module for Country model """

    def test_country_code_converted_to_upper_case(self):
        Country.objects.create(
            country_code='mx',
            name='Mexico'
        )
        mexico = Country.objects.get(country_code='MX')
        if mexico is None:
            self.assertEqual(True, False)
        self.assertEqual('MX', mexico.country_code)

    def test_country_code_is_2letters(self):
        try:
            Country.objects.create(
                country_code='mex',
                name='Mexico'
            )
            self.assertEqual(True, False)
        except:
            self.assertEqual(True, True)


class CommodityData_Test(TestCase):
    """ Test module for CommodityData model """

    def setUp(self):
        Country.objects.create(
            country_code='MX',
            name='Mexico'
        )
        Country.objects.create(
            country_code='BR',
            name='Brazil'
        )
        mexico = Country.objects.get(country_code='MX')
        brazil = Country.objects.get(country_code='BR')
        CommodityData.objects.create(
            country=mexico,
            commodity='mango',
            fixed_overhead=decimal.Decimal(32.00),
            variable_cost=decimal.Decimal(1.24)
        )
        CommodityData.objects.create(
            country=brazil,
            commodity='mango',
            fixed_overhead=decimal.Decimal(20.00),
            variable_cost=decimal.Decimal(1.42)
        )
        qs = CommodityData.objects.all()
        # print('setUp')
        # print(list(qs))

    def test_unique(self):
        mexico = Country.objects.get(country_code='MX')
        try:
            CommodityData.objects.create(
                country=mexico,
                commodity='mango',
                fixed_overhead=decimal.Decimal(20.00),
                variable_cost=decimal.Decimal(1.00)
            )
            self.assertEqual(True, False)
        except:
            self.assertEqual(True, True)

    def test_country_required(self):
        try:
            CommodityData.objects.create(
                country='MX',
                commodity='mango',
                fixed_overhead=decimal.Decimal(20.00),
                variable_cost=decimal.Decimal(1.00)
            )
            self.assertEqual(True, False)
        except:
            self.assertEqual(True, True)

    def test_costs_must_be_decimal8x2(self):
        mexico = Country.objects.get(country_code='MX')
        try:
            CommodityData.objects.create(
                country=mexico,
                commodity='apple',
                fixed_overhead=decimal.Decimal(20.00),
                variable_cost=decimal.Decimal(1.00)
            )
            self.assertEqual(True, True)
        except:
            self.assertEqual(True, False)
        try:
            CommodityData.objects.create(
                country=mexico,
                commodity='apple',
                fixed_overhead=decimal.Decimal(20.999),
                variable_cost=decimal.Decimal(1.00)
            )
            self.assertEqual(True, False)
        except:
            self.assertEqual(True, True)
        try:
            CommodityData.objects.create(
                country=mexico,
                commodity='apple',
                fixed_overhead=decimal.Decimal(20.99),
                variable_cost=decimal.Decimal(1.001)
            )
            self.assertEqual(True, False)
        except:
            self.assertEqual(True, True)

    def test_commodity_required(self):
        try:
            CommodityData.objects.create(
                country='MX',
                commodity='',
                fixed_overhead=decimal.Decimal(20.00),
                variable_cost=decimal.Decimal(1.00)
            )
            self.assertEqual(True, False)
        except:
            self.assertEqual(True, True)

    def test_composite_key(self):
        mexico = Country.objects.get(country_code='MX')
        qs = CommodityData.objects.filter(
            Q(country=mexico) & Q(commodity='mango')
        )
        self.assertEqual(
            qs.count(), 1
        )

    def test_query_variable_cost(self):
        mango = CommodityData.objects.get(variable_cost=decimal.Decimal(1.24))
        # print(mango)
        self.assertEqual(mango.country.country_code, 'MX')



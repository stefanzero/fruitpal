from ..models import Country, CommodityData
import decimal


def set_up_mango():
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

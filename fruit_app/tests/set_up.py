from ..models import Commodity_Data
import decimal


def set_up_mango():
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

from ..models import Commodity_Data
import decimal

def run():
    commodity_data = Commodity_Data()
    commodity_data.country = 'MX'
    commodity_data.commodity = 'mango'
    commodity_data.fixed_overhead=decimal.Decimal(32)
    commodity_data.variable_cost=decimal.Decimal(1.24)
    commodity_data.save()

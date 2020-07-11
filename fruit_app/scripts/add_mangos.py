from ..models import CommodityData
import decimal
import os
import json


def run():
    commodities = get_mangos()
    for commodity in commodities:
        commoditydata = CommodityData()
        commoditydata.country = commodity['country']
        commoditydata.commodity = commodity['commodity']
        commoditydata.fixed_overhead = decimal.Decimal(commodity['fixed_overhead'])
        commoditydata.variable_cost=decimal.Decimal(commodity['variable_cost'])
        try:
            commoditydata.save()
        except:
            print('{} from {} already exists'.format(
                commodity['commodity'], commodity['country']))


def get_mangos():
    return [
        {
            'country': 'MX',
            'commodity': 'mango',
            'fixed_overhead': 32,
            'variable_cost': 1.24
        },
        {
            'country': 'BR',
            'commodity': 'mango',
            'fixed_overhead': 20,
            'variable_cost': 1.42
        },
    ]

def read_commoditydata():
    json_path = os.path.join(os.path.dirname(__file__), 'commodity-data.json')
    with open(json_path, 'r') as input_file:
        commoditydata = json.load(input_file)


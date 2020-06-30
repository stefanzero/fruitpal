from ..models import Commodity_Data
import decimal
import os
import json


def run():
    commodities = get_mangos()
    for commodity in commodities:
        commodity_data = Commodity_Data()
        commodity_data.country = commodity['country']
        commodity_data.commodity = commodity['commodity']
        commodity_data.fixed_overhead = decimal.Decimal(commodity['fixed_overhead'])
        commodity_data.variable_cost=decimal.Decimal(commodity['variable_cost'])
        try:
            commodity_data.save()
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

def read_commodity_data():
    json_path = os.path.join(os.path.dirname(__file__), 'commodity-data.json')
    with open(json_path, 'r') as input_file:
        commodity_data = json.load(input_file)


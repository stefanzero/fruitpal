from ..models import Commodity_Data, Country
import decimal
import os
import json


def run():
    commodities = read_commodity_data()
    for commodity in commodities:
        commodity_data = Commodity_Data()
        # commodity_data.country = commodity['country']
        country = Country.objects.get(country_code=commodity['country'])
        commodity_data.country = country
        commodity_data.commodity = commodity['commodity'].lower()
        commodity_data.fixed_overhead = decimal.Decimal(commodity['fixed_overhead'])
        commodity_data.variable_cost=decimal.Decimal(commodity['variable_cost'])
        try:
            commodity_data.save()
        except:
            print('{} from {} already exists'.format(
                commodity['commodity'], commodity['country']))


def read_commodity_data():
    json_path = os.path.join(os.path.dirname(__file__), 'commodity-data.json')
    with open(json_path, 'r') as input_file:
        commodity_data = json.load(input_file)
    return commodity_data

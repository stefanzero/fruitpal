from ..models import CommodityData, Country
import decimal
import os
import json


def run():
    commodities = read_commoditydata()
    for commodity in commodities:
        commoditydata = CommodityData()
        # commoditydata.country = commodity['country']
        country = Country.objects.get(country_code=commodity['country'])
        commoditydata.country = country
        commoditydata.commodity = commodity['commodity'].lower()
        commoditydata.fixed_overhead = decimal.Decimal(commodity['fixed_overhead'])
        commoditydata.variable_cost=decimal.Decimal(commodity['variable_cost'])
        try:
            commoditydata.save()
        except:
            print('{} from {} already exists'.format(
                commodity['commodity'], commodity['country']))


def read_commoditydata():
    json_path = os.path.join(os.path.dirname(__file__), 'commodity-data.json')
    with open(json_path, 'r') as input_file:
        commoditydata = json.load(input_file)
    return commoditydata

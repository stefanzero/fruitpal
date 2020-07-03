from .sample_data import fruit_data
from .sample_data import country_data
import json
import random
import math
from functools import reduce
import re
import os
from collections import namedtuple

# def run(*args):
#     print(args)

def parse_keywords(a, b):
    matches = re.match(r'^(\w+)\s*=\s*(\w+)$', b)
    if matches and len(matches.groups()) == 2:
        a[matches.group(1)] = matches.group(2)
    return a

def run(*args):
    # create dictionary from pseudo keyword arguments
    # print('args', args)
    arg_dict = reduce(parse_keywords, args, {})
    # print('arg_dict', arg_dict)
    if not arg_dict['num_fruits'] and not arg_dict['num_countries']:
        print('Usage: python manage.py runscript create_commodity_data --script-args num_fruits=n num_countries=m')
        return
    num_fruits = arg_dict['num_fruits']
    try:
        num_fruits = int(num_fruits)
    except:
        print('num_fruits "{}" must be an integer'.format(num_fruits))
        return
    num_countries = arg_dict['num_countries']
    try:
        num_countries = int(num_countries)
    except:
        print('num_countries "{}" must be an integer'.format(num_countries))
        return
    # print('num_countries = {}'.format(num_countries))
    # print('num_fruits = {}'.format(num_fruits))

    country_dict = country_data.get_country_dict()
    countries = country_dict.keys()
    # print(countries)
    fruits = fruit_data.get()
    # print(fruits)
    if num_fruits > len(fruits):
        print('using maximum number of fruits')
        num_fruits = len(fruits)
    if num_countries > len(countries):
        print('using maximum number of countries')
        num_countries = len(countries)
    random_fruits = random.sample(fruits, num_fruits)
    # print(random_fruits)
    Commodity_Data = namedtuple('Commodity_Data', 'country commodity fixed_overhead, variable_cost')
    commodity_list = []
    for fruit in random_fruits:
        if fruit.lower() == 'mango':
            continue
        random_countries = random.sample(countries, num_countries)
        print(fruit, random_countries)
        for country in random_countries:
            fixed_overhead = get_random_value(2)
            variable_cost = get_random_value(1)
            cd = Commodity_Data(
                commodity=fruit, country=country,
                fixed_overhead=fixed_overhead,
                variable_cost=variable_cost)
            # cd = {
            #     'commodity': fruit,
            #     'country': country,
            #     'fixed_overhead': fixed_overhead,
            #     'variable_cost': variable_cost
            # }
            # commodity_list.append(cd)
            commodity_list.append(cd._asdict())

    commodity_json = json.dumps(commodity_list, indent = 2, separators=(',', ': '))
    json_path = os.path.join(os.path.dirname(__file__), 'commodity-data.json')
    with open(json_path, 'w') as output_file:
        output_file.write(commodity_json)


'''
Return a number with 2 decimal places of the specified power
'''
def get_random_value(power):
    a = 10**(power + 2)
    b = 10**(power + 3)
    c = 10**power
    decimal = random.randint(0, 99) / 100
    return math.floor(random.randint(a, b) / 100) + decimal

# def random_countries(n):
#     return random.sample(countries, n)
#
# def random_fruits(n):
#     return random.sample(fruits, n)



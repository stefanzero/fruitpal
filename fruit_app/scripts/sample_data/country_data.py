import json
import os

def get_country_dict():
    file_path = os.path.join(os.path.dirname(__file__), 'countries-2.json')
    with open(file_path) as f:
        countries = json.load(f)
    return countries

def get_country_dict_all():
    file_path = os.path.join(os.path.dirname(__file__), 'countries-0.json')
    with open(file_path) as f:
        countries = json.load(f)
    return countries

from ..models import Country
import decimal
import os
import json
from .sample_data import country_data


def run():
    country_dict = country_data.get_country_dict_all()
    countries = country_dict.keys()
    for country in countries:
        country_model = Country()
        country_model.country = country
        country_model.name = country_dict[country]
        try:
            country_model.save()
        except:
            print('exception for country code {}'.format(country))


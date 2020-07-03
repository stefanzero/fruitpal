from ..models import Commodity_Data, Country
import decimal
import os
import json


def run():
    commodity_data_all = list(Commodity_Data.objects.all())
    for datum in commodity_data_all:
        item = Commodity_Data.objects.get(pk=datum.id)
        print(item)
        item.commodity = item.commodity.lower()
        item.save()


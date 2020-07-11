from ..models import CommodityData, Country
import decimal
import os
import json


def run():
    commoditydata_all = list(CommodityData.objects.all())
    for datum in commoditydata_all:
        item = CommodityData.objects.get(pk=datum.id)
        print(item)
        item.commodity = item.commodity.lower()
        item.save()


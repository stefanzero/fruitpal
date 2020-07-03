import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Commodity_Data
from ..serializers import CommodityDataSerializer
from .set_up import set_up_mango
import decimal


# initialize the APIClient app
client = Client()

class GetAllCommodityDataTest(TestCase):
    """ Test module for GET all commodity_data API """

    def setUp(self):
        set_up_mango()

    def test_get_all_commodity_data(self):
        # get API response
        response = client.get(reverse('get_post_commodity_data'))
        # get data from db
        commodity_data = Commodity_Data.objects.all()
        serializer = CommodityDataSerializer(commodity_data, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CalculateTest(TestCase):
    """ Test module for GET all commodity_data API """

    def setUp(self):
        set_up_mango()

    def test_calculate(self):
        response = client.get('/api/v1/calculate/',
                              {'COMMODITY': 'mango',
                               'PRICE': 53,
                               'TONS': 405}
                              )
        data0 = response.data[0]
        country0 = data0['country']
        total_cost0 = float(data0['total_cost'])
        fixed_overhead0 = float(data0['fixed_overhead'])
        variable_cost0 = float(data0['variable_cost'])
        self.assertEqual(total_cost0, 22060.1)
        self.assertEqual(fixed_overhead0, 20)
        self.assertEqual(variable_cost0, 54.42)

        data1 = response.data[1]
        country1 = data1['country']
        total_cost1 = float(data1['total_cost'])
        fixed_overhead1 = float(data1['fixed_overhead'])
        variable_cost1 = float(data1['variable_cost'])
        self.assertEqual(total_cost1, 21999.20)
        self.assertEqual(fixed_overhead1, 32)
        self.assertEqual(variable_cost1, 54.24)


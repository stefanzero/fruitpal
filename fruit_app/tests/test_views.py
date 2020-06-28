import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Commodity_Data
from ..serializers import CommodityDataSerializer
from .set_up import set_up_mango


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

    def test_calculate(self):
        response = client.get({'commodity': 'mango'})
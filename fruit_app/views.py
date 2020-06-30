from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Commodity_Data
from .serializers import CommodityDataSerializer
from functools import partial
import json
import decimal
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from .serializers import MyJSONRenderer


@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_commodity_data(request, pk):
    try:
        commodity_data = Commodity_Data.objects.get(pk=pk)
    except Commodity_Data.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single item
    if request.method == 'GET':
        return Response({})
    # delete a single puppy
    elif request.method == 'DELETE':
        return Response({})
    # update details of a single item
    elif request.method == 'PUT':
        return Response({})


@api_view(['GET', 'POST'])
def get_post_commodity_data(request):
    # get all items
    if request.method == 'GET':
        commodity_data = Commodity_Data.objects.all()
        serializer = CommodityDataSerializer(commodity_data, many=True)
        return Response(serializer.data)
    # insert a new record for a items
    elif request.method == 'POST':
        return Response({})


@api_view(['GET', 'DELETE', 'PUT'])
@renderer_classes([JSONRenderer])
def get_commodities(request):
    commodity_list = list(Commodity_Data.objects.values('commodity').distinct())
    commodities = list(map(lambda x: x.commodity, commodity_list))
    return Response(commodities)

'''
total cost = number of tons * (price per ton + variable cost) + fixed cost
variable cost (at this price point) = price per ton + variable cost per ton

Return JSON array sorted by total cost descending:
* country code
* total cost of purchase
* variable cost
* fixed cost
'''

@api_view(('GET',))
@renderer_classes([MyJSONRenderer])
def calculate(request, format='json'):
    commodity = request.GET.get('COMMODITY')
    price = request.GET.get('PRICE')
    tons = request.GET.get('TONS')
    if commodity is None or price is None or tons is None:
        return Response({
            'status': 'Bad request',
            'message': 'request must contain query parameters for COMMODITY, PRICE and TONS'
        }, status=status.HTTP_400_BAD_REQUEST)
    commodity = commodity.strip('"').strip("'")
    price = decimal.Decimal(price) if price is not None else 0
    tons = decimal.Decimal(tons) if tons is not None else 0
    print('commodity "{}"'.format(commodity))
    commodities = list(Commodity_Data.objects.filter(commodity=commodity))
    print(commodities)
    map_function = partial(compute_costs, tons=tons, price=price)
    results = list(map(map_function, commodities))
    print('results')
    print(results)
    # results.sort(key=lambda x: x.total_cost, reverse=True)
    return Response(results, status=status.HTTP_200_OK)
    # results_json = list(map(json.dumps, results))
    # return Response({"data": results_json})


def compute_costs(data, tons, price):
    total_cost = tons * (price + data.variable_cost) + data.fixed_overhead
    fixed_cost = data.fixed_overhead
    variable_cost = price + data.variable_cost
    return {
        "country_code": data.country,
        "total_cost": total_cost,
        "variable_cost": variable_cost,
        "fixed_cost": fixed_cost
    }

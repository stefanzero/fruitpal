# from django.shortcuts import render
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import CommodityData, Country
from .serializers import CommodityDataSerializer, CountrySerializer
from functools import partial
import operator
import decimal
from rest_framework.decorators import api_view, renderer_classes
# from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.renderers import JSONRenderer
from .serializers import MyJSONRenderer


@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_commoditydata(request, pk):
    """Restframework API get/delete/put endpoint the CommodityData model


    Args:
        pk (int): Database Id of item in the table
          fruit_app_commoditydata

    Returns:
        str: HTML page with an HTML form

    """
    try:
        commoditydata = CommodityData.objects.get(pk=pk)
    except CommodityData.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single commoditydata
    if request.method == 'GET':
        serializer = CommodityDataSerializer(commoditydata)
        return Response(serializer.data)

    # update details of a single commoditydata
    if request.method == 'PUT':
        serializer = CommodityDataSerializer(commoditydata, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete a single commoditydata
    elif request.method == 'DELETE':
        return Response({})


@api_view(['GET', 'POST'])
def get_post_commoditydata(request):
    """Restframework API post endpoint the CommodityData model


    Args:
        pk (int)
            Database Id of item in the table fruit_app_commoditydata

    Returns:
        str: HTML page with an HTML form

    """
    # get all items
    if request.method == 'GET':
        commoditydata = CommodityData.objects.all()
        serializer = CommodityDataSerializer(commoditydata, many=True)
        return Response(serializer.data)
    # insert a new record for a items
    elif request.method == 'POST':
        return Response({})


@api_view(['GET', 'DELETE', 'PUT'])
@renderer_classes([JSONRenderer])
def get_commodities(request):
    """API get endpoint to return JSON array of commodities


    Returns:
        str: JSON array of commodities

    """
    commodity_list = list(CommodityData.objects.values('commodity').distinct())
    commodities = list(map(lambda x: x['commodity'], commodity_list))
    return Response(commodities)


@api_view(('GET',))
@renderer_classes([MyJSONRenderer])
def calculate(request, format='json'):
    """API get endpoint to calculate the cost for a trade request

    total cost = number of tons * (price per ton + variable cost) + fixed cost
    variable cost (at this price point) = price per ton + variable cost per ton

    Return JSON array sorted by total cost descending:
    * country code
    * total cost of purchase
    * variable cost
    * fixed cost

    Args:
        request (Request)
            Request must have query parameters for COMMODITY, PRICE, and
            TONS

    Returns:
        str: JSON object

    """
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
    # print('commodity "{}"'.format(commodity))
    # commodities = list(CommodityData.objects.filter(commodity=commodity))
    commodities = list(CommodityData.objects.filter(commodity__iexact=commodity))
    # print(commodities)
    map_function = partial(compute_costs, tons=tons, price=price)
    results = list(map(map_function, commodities))
    results.sort(key=operator.itemgetter('total_cost'), reverse=True)
    # results.sort(key=lambda x: x.total_cost, reverse=True)
    # print('results')
    # print(results)
    return Response(results, status=status.HTTP_200_OK)


def compute_costs(data, tons, price):
    """Helper function for calculate

    Args:
        data (dict)

    :param data:
    :param tons:
    :param price:
    :return:
    """
    total_cost = tons * (price + data.variable_cost) + data.fixed_overhead
    fixed_overhead = data.fixed_overhead
    variable_cost = price + data.variable_cost
    return {
        "country": data.country.country_code,
        "total_cost": total_cost,
        "fixed_overhead": fixed_overhead,
        "variable_cost": variable_cost,
    }


@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_country(request, pk):
    """Restframework API get/delete/put endpoint the Country model


    Args:
        pk (int): Database Id of item in the table
          fruit_app_country

    Returns:
        str: HTML page with an HTML form

    """
    try:
        country = Country.objects.get(pk=pk)
    except Country.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single country
    if request.method == 'GET':
        serializer = CountrySerializer(country)
        return Response(serializer.data)

    # update details of a single country
    if request.method == 'PUT':
        serializer = CountrySerializer(country, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete a single country
    elif request.method == 'DELETE':
        return Response({})


@api_view(['GET', 'POST'])
def get_post_country(request):
    """Restframework API post endpoint the Country model


    Args:
        request (Request)

    Returns:
        str: HTML page with an HTML form

    """
    # get all items
    if request.method == 'GET':
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data)
    # insert a new record for a items
    elif request.method == 'POST':
        return Response({})



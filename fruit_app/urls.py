from django.conf.urls import url
from . import views


urlpatterns = [
    url(
        r'^api/v1/commodity_data/(?P<pk>[0-9]+)$',
        views.get_delete_update_commodity_data,
        name='get_delete_update_commodity_data'
    ),
    url(
        r'^api/v1/commodity_data/$',
        views.get_post_commodity_data,
        name='get_post_commodity_data'
    ),
    url(
        r'^api/v1/commodities/$',
        views.get_commodities,
        name='get_commodities'
    ),
    url(
        r'^api/v1/countries/(?P<pk>[0-9]+)$',
        views.get_delete_update_country,
        name='get_delete_update_country'
    ),
    url(
        r'^api/v1/countries/$',
        views.get_post_country,
        name='get_post_country'
    ),
    url(
        r'^api/v1/calculate/$',
        views.calculate,
        name='calculate'
    )
]
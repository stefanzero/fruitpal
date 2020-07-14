from django.conf.urls import url
from . import views


urlpatterns = [
    url(
        r'^api/v1/commoditydata/(?P<pk>[0-9]+)$',
        views.get_delete_update_commoditydata,
        name='get_delete_update_commoditydata'
    ),
    url(
        r'^api/v1/commoditydata/$',
        views.get_post_commoditydata,
        name='get_post_commoditydata'
    ),
    url(
        r'^api/v1/commodities/$',
        views.get_commodities,
        name='get_commodities'
    ),
    url(
        r'^api/v1/countries/(?P<country_code>[A-Z]{2})$',
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
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
        r'^api/v1/calculate/$',
        views.calculate,
        name='calculate'
    )
]
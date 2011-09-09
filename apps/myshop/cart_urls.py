from django.conf.urls.defaults import patterns, url

from .views import MySimplevariationCartDetails


urlpatterns = patterns('',
    url(r'^delete/$',
        MySimplevariationCartDetails.as_view(action='delete'),
        name='cart_delete'),
    url('^item/$',
        MySimplevariationCartDetails.as_view(action='post'),
        name='cart_item_add' ),
    url(r'^$',
        MySimplevariationCartDetails.as_view(), name='cart'),
    url(r'^cart/update/$',
        MySimplevariationCartDetails.as_view(action='put'),
        name='cart_update'),
    url('^item/(?P<id>[0-9A-Za-z-_.//]+)$',
        MySimplevariationCartDetails.as_view(),
        name='cart_item' ),
)

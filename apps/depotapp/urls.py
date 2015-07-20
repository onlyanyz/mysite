from django.conf.urls import patterns, include, url
from django.conf import settings
from rest_framework import routers
import views

urlpatterns = patterns('',
    url(r'^product/create/$',views.create_product),
    url(r'^product/list/$',views.list_product),
    url(r'^product/edit/(?P<id>[^/]+)/$',views.edit_product),
    url(r'^product/view/(?P<id>[^/]+)/$',views.view_product),
    url(r'^store/$',views.store_view),
    url(r'^cart/view/$',views.view_cart),
    url(r'^cart/add/(?P<id>[^/]+)/$',views.add_to_cart),
    url(r'^cart/clean/$',views.clean_cart),

    url(r'^api/cart/items',views.cart_item_list),
)

# router=routers.DefaultRouter()
# router.register(r'cart',views.LineItemViewSet,base_name='depotapp')

# urlpatterns+=patterns('',
#     # url(r'^',include(router.urls)),
#     # url(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework'))
# )

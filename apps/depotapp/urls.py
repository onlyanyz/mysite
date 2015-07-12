from django.conf.urls import patterns, include, url
from django.conf import settings
import views

urlpatterns = patterns('',
    url(r'^product/create/$',views.create_product),
    url(r'^product/list/$',views.list_product),
    url(r'^product/edit/(?P<id>[^/]+)/$',views.edit_product),
    url(r'^product/view/(?P<id>[^/]+)/$',views.view_product),
)

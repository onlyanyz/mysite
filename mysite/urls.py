from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # (r'^.*js/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_JS}),
    # (r'^.*css/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_CSS}),
    # (r'^.*images/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_IMG}),
    # (r'^.*fonts/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_FONTS}),
)

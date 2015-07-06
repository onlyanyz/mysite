#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static  # use to display media resources such as images

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^.*js/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_JS}),
    (r'^.*css/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_CSS}),
    (r'^.*images/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_IMG}),
    (r'^.*fonts/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_FONTS}),

    url(r'^$','mysite.views.index'),
    url(r'^home/$',include('apps.blog.urls')),
)

# 设置下面两行用于在管理界面点击图片地址时可以进行查看
urlpatterns += patterns('',
)+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

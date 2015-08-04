from django.conf.urls import patterns, include, url
# from django.conf import settings
import views

urlpatterns=patterns('',
    url(r'^$',views.todolist),
    url(r'^addtodo/$',views.addtodo,name='add'),
    url(r'^todofinish/(?P<id>\d+)/$',views.todofinish),
    url(r'^updatetodo/(?P<id>\d+)/$',views.updatetodo),
    url(r'^tododelete/(?P<id>\d+)/$',views.tododelete),
    url(r'^todoback/(?P<id>\d+)/$',views.todoback),
    url(r'^account/login/$',views.login_view),
    url(r'^account/logout/$',views.logout_view),
    url(r'^account/register/$',views.register),
    url(r'^login/$',views.login_page),

    url(r'^base/$',views.base),
)
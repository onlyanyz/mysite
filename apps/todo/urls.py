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
)
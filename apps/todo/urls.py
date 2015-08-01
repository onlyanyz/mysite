from django.conf.urls import patterns, include, url
# from django.conf import settings
import views

urlpatterns=patterns('',
    url(r'^$',views.todolist),
    url(r'^addtodo/$',views.addtodo,name='add'),
)
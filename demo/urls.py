from django.conf.urls import url
from . import views

app_name = 'demo'
urlpatterns = [
    # /
    url(r'^$', views.index, name='index'),

    # /object/myobject
    url(r'^object/(?P<object_name>[a-zA-Z0-9\-]+)/$', 
        views.details, name='details'),

    # /edit/myobject
    url(r'^edit/(?P<object_name>[a-zA-Z0-9\-]+)/$', 
        views.edit, name='edit'),

    # /store/myobject
    url(r'^store/(?P<object_name>[a-zA-Z0-9\-]+)/$', 
        views.store, name='store'),

    # /delete/myobject
    url(r'^delete/(?P<object_name>[a-zA-Z0-9\-]+)/$', 
        views.delete, name='delete'),

    # /create
    url(r'^create/$', views.create, name='create'),

    # /store_new
    url(r'^store_new/$', views.store_new, name='store_new'),
]

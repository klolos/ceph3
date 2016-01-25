from django.conf.urls import url
from . import views

app_name = 'demo'
urlpatterns = [
    # /
    url(r'^$', views.index, name='index'),

    # /object/myobject
    url(r'^object/(?P<object_name>[a-zA-Z0-9\-]+)/$', 
        views.details, name='details'),

    # /object/myobject/edit
    url(r'^object/(?P<object_name>[a-zA-Z0-9\-]+)/edit/$', 
        views.edit, name='edit'),

    # /object/myobject/update
    url(r'^object/(?P<object_name>[a-zA-Z0-9\-]+)/update/$', 
        views.update, name='update'),

    # /object/myobject/delete
    url(r'^object/(?P<object_name>[a-zA-Z0-9\-]+)/delete/$', 
        views.delete, name='delete'),

    # /create
    url(r'^create/$', views.create, name='create'),

    # /store
    url(r'^store/$', views.store, name='store'),
]

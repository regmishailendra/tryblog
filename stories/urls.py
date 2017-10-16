from django.conf.urls import url, include
from . import views
urlpatterns = [


    url(r'^create/$',views.create,name='create'),
    url(r'^(?P<id>\d+)/details/$',views.details,name='details'),
    url(r'^(?P<id>\d+)/edit/$',views.edit,name='edit'),
    url(r'^(?P<id>\d+)/delete/$',views.delete,name='delete'),


]

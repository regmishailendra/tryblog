from django.conf.urls import url, include

from . import views
urlpatterns = [

    url(r'^$',views.StoryListAPIView.as_view(),name='listapi'),
    url(r'^create/$',views.StoryCreateAPIView.as_view(),name='createapi'),

#    url(r'^image/$',views.AvatarView.as_view()),


    url(r'^(?P<pk>\d+)/details/$',views.StoryDetailAPIView.as_view(),name='detailsapi'),
    url(r'^(?P<pk>\d+)/edit/$',views.StoryUpdateAPIView.as_view(),name='editapi'),
    url(r'^(?P<pk>\d+)/delete/$',views.StoryDeleteAPIView.as_view(),name='deleteapi'),


]




#^(?P<title>[\w-]+)/$
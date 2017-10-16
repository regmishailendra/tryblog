from django.conf.urls import url

from accounts.api.views import UserCreateAPIView, UserLoginAPIView

urlpatterns=[

    url(r'^register/$', UserCreateAPIView.as_view(),name='registerapi'),
    url(r'^login/$', UserLoginAPIView.as_view(),name='loginapi'),





]
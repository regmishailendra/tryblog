from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token

from stories import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^stories/', include('stories.urls'),name='stories'),
    url(r'^login/', views.login_view,name='login'),
    url(r'^register/',  views.register_view,name='register'),
    url(r'^logout/', views.logout_view, name='logout'),
    #url(r'^', views.list, name='list'),
    url(r'^api/', include('stories.api.urls')),
    url(r'^api/users/', include('accounts.api.urls')),
url(r'^api/auth/token', obtain_jwt_token),

    url(r'^$', views.list, name='list'),    #brought here from stories app for frontpage

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

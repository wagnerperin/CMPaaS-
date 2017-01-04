from api import views
from django.conf.urls import url, include
from django.http import HttpResponse

from django.contrib import admin 
admin.autodiscover()

from rest_framework import permissions, routers, serializers, viewsets
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope

from rest_framework.routers import DefaultRouter
from rest_framework_extensions.routers import ExtendedDefaultRouter
from django.contrib import admin

def index(request):
	return HttpResponse("CMPaaS API.")

router = ExtendedDefaultRouter()
(
    router.register(r'maps', views.MapViewSet, base_name='map')
          .register(r'versions',
                    views.VersionViewSet,
                    base_name='maps-version',
                    parents_query_lookups=['map'])
)

router.register(r'users', views.UserViewSet)

urlpatterns = [
	url(r'^$', index, name='index'),
	url(r'^api/', include(router.urls)),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^admin/', admin.site.urls),
	url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider'))
]

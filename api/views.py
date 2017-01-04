from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from api.models import Map, Version
from api.permissions import IsOwnerOrReadOnly
from api.serializers import MapSerializer, VersionSerializer, UserSerializer
from rest_framework_extensions.mixins import NestedViewSetMixin

class MapViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    This endpoint presents conceptual maps.
    """
    queryset = Map.objects.all()
    serializer_class = MapSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class VersionViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    This endpoint presents version of conceptual maps.
    """
    queryset = Version.objects.all()
    serializer_class = VersionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def filter_queryset(self, queryset):
        queryset = super(VersionViewSet, self).filter_queryset(queryset)
        return queryset.order_by('-updated')
    
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This endpoint presents the users in the system.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
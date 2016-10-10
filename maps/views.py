from .models import Map
from rest_framework import viewsets
from .serializers import MapSerializer

class MapViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Map.objects.all()
    serializer_class = MapSerializer
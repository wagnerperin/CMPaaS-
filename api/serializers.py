from rest_framework import serializers
from api.models import Map, Version
from django.contrib.auth.models import User


class MapSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Map
        fields = ('url', 'author', 'title', 'question', 'description')
        read_only_fields = ['author']

class VersionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Version
        fields = ('id', 'updated', 'map', 'author' , 'content')
        read_only_fields = ['author']
                  
class UserSerializer(serializers.HyperlinkedModelSerializer):
    maps = serializers.HyperlinkedRelatedField(queryset=Map.objects.all(), view_name='map-detail', many=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'maps')


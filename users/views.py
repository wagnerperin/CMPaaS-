from django.contrib.auth.models import User, Group
from rest_framework.response import Response
from .models import Profile
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, GroupSerializer, ProfileSerializer
from rest_framework.decorators import detail_route, list_route
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    @detail_route(methods=['delete'])
    def remove_profile(self, request, pk):
        profile = Profile.objects.get(pk=pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
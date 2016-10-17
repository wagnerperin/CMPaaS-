from django.contrib.auth.models import User, Group
from rest_framework.response import Response
from .models import Profile
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, GroupSerializer, ProfileSerializer, RegistrationSerializer
from rest_framework.decorators import detail_route, list_route
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope

from rest_framework.views import APIView
from rest_framework import status




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


# Just the POST method is coded, so we don't need a viewset
class RegistrationView(APIView):
    """ Allow registration of new users. """
    permission_classes = ()

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)

        # Check format and unique constraint
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        data = serializer.data

        u = User.objects.create(username=data['username'],
                                email=data['email'],
                                first_name=data['first_name'],
                                last_name=data['last_name'],)
        u.set_password(data['password'])
        u.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

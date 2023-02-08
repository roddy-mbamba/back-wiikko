
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from api.serializers import UserSerializer
from api.models import *

class UserViewsSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_classes = (IsAuthenticated,)
    #filterset_fields = ['nom']
    #search_fields = ['nom']
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserSerializer
        else:
            return self.serializer_class
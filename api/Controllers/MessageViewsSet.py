from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from api.serializers import MessageSerializer
from api.models import *

class MessageViewsSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)
    #filterset_fields = ['nom']
    #search_fields = ['nom']
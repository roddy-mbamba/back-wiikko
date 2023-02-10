
import datetime
from rest_framework import viewsets
#from rest_framework.permissions import IsAuthenticated
from api.serializers import MessageSerializer
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed 
from rest_framework.response import Response
from api.models import *

class MessageViewsSet(APIView):

    def get(self, request,user_envoyer):
        tokken=request.COOKIES.get('jwt')
        if(not tokken):
            raise  AuthenticationFailed("L'authentification est requise pour cette opération")
        messages = Message.objects.filter(users__id=user_envoyer)
        message_arrange=[]
       
        for message in messages:
            message_arrange.append({
                "id":message.id,
                "msg":message.msg,
                "envoyer":message.users.first().username,
                "destination":message.users.all()[1].username,
                "createAt":message.createAt.date(),
            })
        return  Response(message_arrange)
    
    def post(self, request):
        tokken=request.COOKIES.get('jwt')
        if(not tokken):
            raise  AuthenticationFailed("L'authentification est requise pour cette opération")
        try:
            message = Message()
            serializer = MessageSerializer(message, data=request.data)
            if serializer.is_valid():
                message.msg=request.data["msg"]
                message.save()
                message.users.add(User.objects.get(request.data["envoyer"]))
                message.users.add(User.objects.get(request.data["destination"]))
                return Response({"message":"Ajouter avec succès"})
            else:
                return Response({"message":"Erreur de validation"})

        except Exception as ex:
            return Response({"message":"Erreur "+str(ex)})


from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from api.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed 
from rest_framework.response import Response
import  jwt,datetime
from api.models import *

class UserViewsSet(APIView):

    def get(self, request):
        tokken=request.COOKIES.get('jwt')
        if(not tokken):
            raise  AuthenticationFailed("L'authentification est requise pour cette opération")
        users = User.objects.all().values()
        return  Response(users)
        return Response({"cookies":tokken})
    
    def post(self, request):
        tokken=request.COOKIES.get('jwt')
        if(not tokken):
            raise  AuthenticationFailed("L'authentification est requise pour cette opération")
        try:
            user = User()
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            """
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid(raise_exception=True):
                user.username = request.data["username"]
                user.last_name = request.POST["last_name"]
                user.first_name = request.POST["first_name"]
                user.email = request.data["username"]
                user.set_password(request.data["password"])
                user.save()
                return Response({"message":"Ajouter avec succès"})
            else:
                return Response({"message":"Erreur de validation"})
            """
        except Exception as ex:
            return Response({"message":"Erreur "+str(ex)})

class  LoginViewsSet(APIView):
    def post(self,request):
        try:
            user=User.objects.filter(username=request.data["username"]).first()
            if(user is None):
                raise AuthenticationFailed("Nom d'utilisateur incorrect")
            if(not user.check_password( request.data["password"])):
                raise AuthenticationFailed("Mot de passe incorrect")
            payload={
                'id':user.id,
                'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=60),
                'iat':datetime.datetime.utcnow()
            }
            tokken=jwt.encode(payload,"ll%mt2&$_*",algorithm='HS256')
            reponse=Response()
            reponse.set_cookie(key='jwt',value=tokken)
            return reponse

        except Exception as ex:
            return  Response({
                'message':'Erreur '+str(ex)
            }) 
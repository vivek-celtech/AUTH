from django.http import JsonResponse
from rest_framework.response import Response
#from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer
from django.contrib.auth import get_user_model

from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        

        return token
    

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer





@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/token/refresh',
    ]

    return Response(routes)


@api_view(['POST'])
@parser_classes([JSONParser])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = get_user_model().objects.create_user(
            username=request.data['username'],
            password=request.data['password'],
            email=request.data['email'],
            status_toggle=request.data.get('status_toggle', False)  # Use the actual field name from your model
        )
        refresh = RefreshToken.for_user(user)
        return Response({'refresh': str(refresh), 'access': str(refresh.access_token), 'user': serializer.data, 'message': 'Account Created Successfully.'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from rest_framework.views import APIView
from rest_framework import generics , status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .serializers import UserSerializer , LoginSerializer

class UserView(generics.CreateAPIView):
    permission_classes = [AllowAny,]
    serializer_class = UserSerializer
class LoginView(APIView):
  permission_classes = [AllowAny,]
  @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='email id'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='user password'),
            },
            required=['email','password']
        )
    )

  def post(self,request):
      
      try:
             serializer_class   = LoginSerializer(data = request.data)
             if serializer_class.is_valid(raise_exception=True):
                 user = authenticate(username = serializer_class.validated_data['username'],password = serializer_class.validated_data['password'])
             if user:
                refresh = RefreshToken.for_user(user)
                return Response(
                    {
                        'Refresh_Token':str(refresh),
                        'Access_Token':str(refresh.access_token)
                    })
             else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
      except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
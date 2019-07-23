from .serializers import UserSerializer,CustomLoginSerializer,CustomRegisterSerializer,LoginSerializer
from .models import CustomerUser
from rest_framework import generics
from rest_auth.views import LoginView, LogoutView
from rest_auth.registration.views import RegisterView
from rest_framework.response import Response
from rest_framework import status
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth import authenticate, login
from rest_framework.parsers import JSONParser
from rest_framework import serializers
from django.http import HttpResponse, JsonResponse



from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.debug import sensitive_post_parameters

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny



class RegisterUserView(generics.ListCreateAPIView):
    queryset = CustomerUser.objects.all()
    serializer_class = CustomRegisterSerializer

    def post(self, request):
        serializer = CustomRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save(request)
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return Response({'received data': request.data}, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors ,status=status.HTTP_400_BAD_REQUEST)



class CustomLogin(LoginView):
    authentication_classes = (SessionAuthentication, )
    queryset = CustomerUser.objects.all()
    serializer_class = CustomLoginSerializer




class CustomLogout(LogoutView):
    queryset = CustomerUser.objects.all()
    serializer_class = CustomLoginSerializer


class UserView(generics.ListCreateAPIView):
    queryset = CustomerUser.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomerUser.objects.all()
    serializer_class = UserSerializer



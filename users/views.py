from .serializers import UserSerializer,CustomLoginSerializer,CustomRegisterSerializer, NameSerializer, PasswordSerializer
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

    # 직렬화? http://raccoonyy.github.io/drf3-tutorial-1.html
    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None: 
            login(request, user)     
            return Response(request.data, status=status.HTTP_201_CREATED)

        else:
            return Response({'error' : 'error'})




class CustomLogout(LogoutView):
    queryset = CustomerUser.objects.all()
    serializer_class = CustomLoginSerializer


class UserView(generics.ListCreateAPIView):
    queryset = CustomerUser.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomerUser.objects.all()
    serializer_class = UserSerializer

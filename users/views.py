from .serializers import UserSerializer,CustomLoginSerializer,CustomRegisterSerializer,LoginSerializer
from .models import CustomerUser
from rest_framework import generics
from rest_auth.views import LoginView, LogoutView
from rest_auth.registration.views import RegisterView
from rest_framework.response import Response
from rest_framework import status
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from rest_framework.parsers import JSONParser
from rest_framework import serializers
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes

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
from rest_framework.parsers import FileUploadParser
from rest_framework import authentication, permissions

# class CustomLoginView(LoginView):
#     def get_response(self):
#         orginal_response = super().get_response()
#         mydata = {"message": "some message", "status": "success"}
#         orginal_response.data.update(mydata)
#         #return orginal_response
#         return Response({'mydata' : mydata}, status=status.HTTP_201_CREATED)


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
                #return Response({'received data': json}, status=status.HTTP_201_CREATED)
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors ,status=status.HTTP_400_BAD_REQUEST)

class CustomLogin(LoginView):
    authentication_classes = (authentication.TokenAuthentication,)
    queryset = CustomerUser.objects.all()
    serializer_class = CustomLoginSerializer


    # def get_queryset(self):
    # user = self.request.user
    # return Purchase.objects.filter(purchaser=user


class CustomLogout(LogoutView):
    queryset = CustomerUser.objects.all()
    serializer_class = CustomLoginSerializer


class UserView(generics.ListCreateAPIView):
    queryset = CustomerUser.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomerUser.objects.all()
    serializer_class = UserSerializer


       

# class FileView(APIView):

#     def get_object(self, pk):
#         try:
#             return CustomerUser.objects.get(pk=pk)
#         except CustomerUser.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         customeruser = self.get_object(pk)
#         serializer = UserSerializer(customeruser)
#         return Response(serializer.data) 

#     def put(self, request, pk, format=None):
#         UserDetailView = self.get_object(pk)
#         serializer = SnippetSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

    # def post(self, request, *args, **kwargs):
    # parser_class = (FileUploadParser,)
    #   file_serializer = FileSerializer(data=request.data)

    #   if file_serializer.is_valid():
    #       file_serializer.save()
    #       return Response(file_serializer.data, status=status.HTTP_201_CREATED)
    #   else:
    #       return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # def delete(self, request, pk, format=None):
    #     snippet = self.get_object(pk)
    #     snippet.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
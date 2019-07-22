from rest_framework.serializers import ModelSerializer, Serializer
from .models import CustomerUser
from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.serializers import LoginSerializer
from rest_framework import serializers

from allauth.account.adapter import get_adapter
from allauth.account import app_settings as allauth_settings
#from allauth.utils import (email_address_exists, get_username_max_length)
#from allauth.account.utils import setup_user_email

class CustomLoginSerializer(ModelSerializer,LoginSerializer):
    class Meta:
        model = CustomerUser
        fields = ['username','password','id']

class CustomRegisterSerializer(ModelSerializer,RegisterSerializer):
    class Meta:
        model = CustomerUser
        fields = ['username','password1','password2','id']


    def validate_id(self,id):
        id = get_adapter().clean_id(id)
        return id


    def validate_username(self, username):
        username = get_adapter().clean_username(username)
        return username

    #def validate_image(self, image):
    #     image = get_adapter().clean_image(image)
    #    return image   

    def validate_password1(self, password):
        return get_adapter().clean_password(password)    

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(("The two password fields didn't match."))
        return data

    def custom_signup(self, request, user):
        pass

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'id' : self.validated_data.get('id', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()

        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        return user
        
class CustomSerializer(ModelSerializer):
    class Meta:
        model = CustomerUser
        fields = ['id', 'username', 'user_photo']


class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomerUser
        fields = ['id', 'username',"user_photo"]


class NameSerializer(ModelSerializer):
    class Meta:
        model = CustomerUser
        fields = ['username',]

class PasswordSerializer(ModelSerializer):
    class Meta:
        model = CustomerUser
        fields = ['password',]


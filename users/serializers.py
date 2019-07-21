from rest_framework.serializers import ModelSerializer 
from .models import CustomerUser 

class UserSerializer(ModelSerializer):    
    class Meta:        
        model = CustomerUser        
        fields = '__all__' # ['id', 'username', 'user_photo']


class CustomSerializer(ModelSerializer):
    class Meta:
        model = CustomerUser
        fields = ['username', 'user_photo']
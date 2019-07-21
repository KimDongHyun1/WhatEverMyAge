from rest_framework import generics 
from .serializers import UserSerializer, CustomSerializer
from .models import CustomerUser 


class UserListView(generics.ListCreateAPIView):    
    queryset = CustomerUser.objects.all()    
    serializer_class = UserSerializer

class CustomListView(generics.RetrieveUpdateDestroyAPIView):    
    queryset = CustomerUser.objects.all()    
    serializer_class = CustomSerializer



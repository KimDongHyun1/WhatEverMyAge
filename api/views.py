from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, MultiPartParser
from .models import Pictures
from .serializers import PictureSerializer
from rest_framework import status

class UserUploadedPicture(APIView):

    def get(self, request, format=None):
        pictures = Pictures.objects.all()
        serializer = PictureSerializer(pictures, many=True)
        return Response(serializer.data)

    parser_classes = (MultiPartParser, JSONParser)
    def post(self, request, *args, **kwargs):
        file_serializer = PictureSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
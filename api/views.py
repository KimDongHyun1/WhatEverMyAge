from rest_framework.parsers import MultiPartParser, FormParser, JSONParser,FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import PictureSerializer
from django.http import JsonResponse

class UserUploadedPicture(APIView):
    parser_classes = (MultiPartParser, )

    def post(self, request, format=None):
        print(request.data)
        print("\n\n\n")
        serializer = PictureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
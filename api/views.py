from rest_framework.parsers import MultiPartParser, FormParser, JSONParser,FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import PostSerializer,PictureSerializer
from django.http import JsonResponse
from .models import Post, Pictures
from rest_framework import viewsets
from rest_framework.decorators import api_view

class UserUploadedPicture(APIView):
    parser_classes = (MultiPartParser, JSONParser) #FormParser

    def get(self, request, format=None):
        pictures = Pictures.objects.all()
        serializer = PictureSerializer(pictures, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
            file_serializer = PictureSerializer(data=request.data)
            if file_serializer.is_valid():
                    file_serializer.save()
                    return Response(file_serializer.data, status=status.HTTP_201_CREATED)
            else:
                    return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def post(self, request, format=None):
    #     print(request.data)
    #     print("\n\n\n")
    #     serializer = PictureSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data)
    #     return JsonResponse(serializer.errors, status=400)

@api_view(['GET', 'POST'])
def post_list(request):

    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


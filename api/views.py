from rest_framework.parsers import MultiPartParser, FormParser, JSONParser,FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import PostSerializer#,PictureSerializer
from django.http import JsonResponse
from .models import Post
from rest_framework import viewsets
from rest_framework.decorators import api_view

# class UserUploadedPicture(APIView):
#     parser_classes = (MultiPartParser, )

#     def post(self, request, format=None):
#         print(request.data)
#         print("\n\n\n")
#         serializer = PictureSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

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


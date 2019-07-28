from rest_framework import viewsets
from .models import Posting, Comment
from .serializers import PostingSerializer, CommentSerializer, PostingDetailSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt  
from django.http import JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser,FileUploadParser
from rest_framework.decorators import api_view
from rest_framework import generics

class PostingList(generics.ListCreateAPIView):
    queryset = Posting.objects.all()
    serializer_class = PostingSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)     



# @api_view(['GET', 'POST'])
# def post_list(request):   

#     if request.method == 'GET':
#         postings = Posting.objects.all()
#         serializer = PostingSerializer(postings, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = PostingSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user) 



@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, pk):
    try:
        posting = Posting.objects.get(pk=pk)
    except Posting.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostingSerializer(posting)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PostingSerializer(posting, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        posting.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)  


class PostingViewSet(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser,JSONParser)
    queryset = Posting.objects.all()
    serializer_class = PostingSerializer
#    permission_classes = [IsAuthenticated]

#    def perform_create(self, serializer):
#        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# @csrf_exempt
# def posting_detail(request, pk):
#     try:
#         posting = Posting.objects.get(pk=pk)
#     except Posting.DoesNotExist:
#         return JsonResponse({'POSTING DOES NOT':'POSTING DOES NOT'}, status=400)
    
#     if request.method == 'GET':
#         serializer = PostingDetailSerializer(posting, context={'request': request})
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = PostingDetailSerializer(posting, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse({'PUT ERROR':'PUT ERROR'}, status=400)

#     elif request.method == 'DELETE':
#         posting.delete()
#         return JsonResponse({'DELETE SUCCESS':'DELETE SUCCESS'}, status=204)


#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)

@csrf_exempt
def post_comments(request, pk):
    try:
        comments = Posting.objects.get(pk=pk).comment_set.all()
    except Posting.DoesNotExist:
        return JsonResponse({'POSTING DOES NOT':'POSTING DOES NOT'})
    except Comment.DoesNotExist:
        return JsonResponse({'COMMENT DOES NOT':'COMMENT DOES NOT'})
    if len(comments) == 0:
        return JsonResponse({'COMMENT IS 0':'COMMENT IS 0'})
    
    if request.method == 'GET':
        serializer = CommentSerializer(comments, many=True)
        return JsonResponse(serializer.data, safe=False)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
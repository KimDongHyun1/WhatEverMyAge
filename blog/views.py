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

#    def perform_create(self, serializer):
#        serializer.save(author=self.request.user)     


class PostingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Posting.objects.all()
    serializer_class = PostingSerializer




class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

#    def perform_create(self, serializer):
#        serializer.save(author=self.request.user)

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

#    def perform_create(self, serializer):
#        serializer.save(author=self.request.user)
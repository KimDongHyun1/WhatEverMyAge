from rest_framework import viewsets
from .models import Posting, Comment, Like
from .serializers import PostingSerializer, CommentSerializer, PostingDetailSerializer, LikeSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt  
from django.http import JsonResponse
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser, FileUploadParser
from rest_framework.decorators import api_view
from rest_framework import generics
from django.http import JsonResponse



@api_view(['GET', 'POST'])
def posting_list(request):
    parser_classes = (MultiPartParser, JSONParser)
    if request.method == 'GET':
        posting = Posting.objects.all()
        serializer = PostingSerializer(posting, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PostingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def aaa(request, pk):
    if request.method == 'GET':
        posting = Posting.objects.get(pk=pk)
        count = posting.like + 1
        Posting.objects.filter(pk=pk).update(like=count)
        return Response({'like++': 'like++'})

        

@api_view(['GET', 'PUT', 'DELETE'])
def posting_detail(request, pk):
    parser_classes = (MultiPartParser, JSONParser)
    try:
        comments = Posting.objects.get(pk=pk).comment_set.all() 
        Posting.objects.filter(pk=pk).update(cnt=len(comments)) # Posting의 CNT 댓글카운트 세는거 늘리기
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



class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

#    def perform_create(self, serializer):
#        serializer.save(author=self.request.user)


class PostingList(generics.ListCreateAPIView):
    
    parser_classes = (MultiPartParser, JSONParser)
    queryset = Posting.objects.all()
    serializer_class = PostingSerializer





@csrf_exempt
def post_comments(request, pk):
    try:
        comments = Posting.objects.get(pk=pk).comment_set.all() 
        Posting.objects.filter(pk=pk).update(cnt=len(comments)) # Posting의 CNT 댓글카운트 세는거 늘리기
    except Posting.DoesNotExist:
        return JsonResponse({'POSTING DOES NOT':'POSTING DOES NOT'})
    except Comment.DoesNotExist:
        return JsonResponse({'COMMENT DOES NOT':'COMMENT DOES NOT'})
    if len(comments) == 0:
        return JsonResponse({'COMMENT IS 0':'COMMENT IS 0'})

    if request.method == 'GET':
        serializer = CommentSerializer(comments, many=True)
        return JsonResponse(serializer.data, safe=False)
    

@api_view(['GET', 'POST'])
def like_list(request):
    if request.method == 'GET':
        like = Like.objects.all()
        serializer = LikeSerializer(like, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST',])  
def like_detail(request, pk):
    like = Like.objects.get(pk=pk)
    like.likeCnt = 100
    like.save()
    return Response({'good':'good'})
from rest_framework import viewsets
from .models import Blog, Comment
from .serializers import BlogSerializer, CommentSerializer, BlogDetailSerializer, CommentreSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt  

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer






class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


@csrf_exempt
def blog_detail(request, pk):
    try:
        blog = Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
        return HttpResponse(status=404)

    if(request.method=='GET'):
        serializer = BlogDetailSerializer(Blog, context={'request':request})
        return JsonResponse(serializer.data)



@csrf_exempt
def blog_comment(request, pk):
    try:
        comment = Blog.objects.get(pk=pk).comment_set.all() # 이걸로 댓글 모으기!!
    except Blog.DoesNotExist:
        return HttpResponse(status=404)
    except Comment.DoesNotExist:
        return HttpResponse(status=404)
    if(len(comment) == 0 ):
        return HttpResponse(status=404)

    if(request.method=='GET'):
        serializer = CommentreSerializer(comment, many=True)
        return JsonResponse(serializer.data, safe=False)


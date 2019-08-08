from rest_framework import viewsets
from .models import Question, Q_Comment
from .serializers import (QuestionSerializer, QuestionDetailSerializer, Q_CommentSerializer, Q_CommentreSerializer) 
from django.http import JsonResponse, HttpResponse  
from django.views.decorators.csrf import csrf_exempt  
from rest_framework.parsers import JSONParser, MultiPartParser


class QuestionViewSet(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser, JSONParser)
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


@csrf_exempt
def question_detail(request, pk):
    parser_classes = (MultiPartParser, JSONParser)
    try:
        question = Question.objects.get(pk=pk)
    except Question.DoesNotExist:
        return JsonResponse({'no': 'no'}, status=400)

    if request.method == 'GET':
        serializer = QuestionDetailSerializer(question, context={'request':request})
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = QuestionDetailSerializer(question, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        question.delete()
        return HttpResponse(status=204)


class Q_CommentViewSet(viewsets.ModelViewSet):
    queryset = Q_Comment.objects.all()
    serializer_class = Q_CommentSerializer


@csrf_exempt
def question_q_comment(request, pk):
    try:
        q_comment = Question.objects.get(pk=pk).q_comment_set.all() # 이걸로 댓글 모으기!!
    except Question.DoesNotExist:
        return HttpResponse(status=404)
    except Q_Comment.DoesNotExist:
        return HttpResponse(status=404)
    if(len(q_comment) == 0 ):
        return HttpResponse(status=404)

    if(request.method=='GET'):
        serializer = Q_CommentreSerializer(q_comment, many=True)
        return JsonResponse(serializer.data, safe=False)
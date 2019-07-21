from django.urls import path, include
from .models import Question, Q_Comment
from rest_framework import serializers

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ['q_title', 'q_content', 'q_created'] #pr


class QuestionDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ['q_title','q_content', 'q_created'] #pr


class Q_CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Q_Comment
        fields = ['question', 'q_reply', 'q_c_created'] #'url' 넣으면안됨


class Q_CommentreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Q_Comment
        fields = ['q_reply', 'q_c_created','q_c_updated']


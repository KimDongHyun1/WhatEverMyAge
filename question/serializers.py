from django.urls import path, include
from .models import Question, Q_Comment
from rest_framework import serializers

class QuestionSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Question
        fields = '__all__'

#아직안씀
class QuestionDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ['q_title','q_content', 'q_created','cnt']


class Q_CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Q_Comment
        fields = ['id','question','author_username','author_id','q_reply','q_c_created','q_c_updated']

class Q_CommentreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Q_Comment
        fields = ['q_reply', 'q_c_created','q_c_updated']


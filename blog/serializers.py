from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Posting, Comment, Like
from rest_framework.fields import ReadOnlyField



class PostingSerializer(serializers.ModelSerializer):
#    author_username = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Posting
        fields = '__all__'





class PostingDetailSerializer(serializers.HyperlinkedModelSerializer):
#    author_username = ReadOnlyField(source='author.username')
   
    class Meta:
        model = Posting
        fields = ('title','id','content')



class CommentSerializer(serializers.ModelSerializer):
    #author_username = ReadOnlyField(source='author.username')
    #posting = ReadOnlyField(source='posting')
    class Meta:
        model = Comment
        fields = ('posting','reply','id','author_username','author_id')

class LikeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Like
        fields = ('userId', 'postingId', 'likeCnt')
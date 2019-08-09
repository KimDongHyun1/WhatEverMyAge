from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Posting, Comment, Love
from rest_framework.fields import ReadOnlyField


class PostingSerializer(serializers.ModelSerializer):
#    author_username = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Posting
        fields = '__all__'


class PostingDetailSerializer(serializers.HyperlinkedModelSerializer):
   
    class Meta:
        model = Posting
        fields = ('title','id','content')



class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('posting','reply','id','author_username','author_id')


class LoveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Love
        fields = '__all__'
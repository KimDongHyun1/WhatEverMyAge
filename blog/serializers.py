from django.urls import path, include
from .models import Blog, Comment
from rest_framework import serializers

class BlogSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Blog
        fields = ('photo','title') #('title','content','like','photo','gps','created','updated','id') #'user',


class BlogDetailSerializer(serializers.HyperlinkedModelSerializer):
    #owner = serializers.ReadOnlyField(source='owner.username')
    #comment = serializers.PrimaryKeyRelatedField(many=True, queryset=Comment.objects.all())#이걸로 뭘 해야함 디테일에서 쪼로록 나올려면

    class Meta:
        model = Blog
        fields = ['title','content','photo']


class CommentSerializer(serializers.HyperlinkedModelSerializer): #Hyperlinked
    class Meta:
        model = Comment
        fields = ['blog','reply','c_created','user'] #'blog','url' 넣으면안됨
        #물어보기 'blog'를 넣으면 댓글은 달리는데  ## api/v1/blog/comment에서 댓글쓰고 POST하기됨
        # blog/<int:pk>/comment/를 들어가면 안됨

class CommentreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ['reply','c_created','c_updated']


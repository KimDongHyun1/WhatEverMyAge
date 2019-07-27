from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Posting, Comment
from rest_framework.fields import ReadOnlyField

class PostingSerializer(serializers.ModelSerializer): #Hyperlinked
    #author_username = ReadOnlyField(source='author.username')
    class Meta:
        model = Posting
        fields = ('title','id') #('id','author_username','title','like','content','photo','gps','created','updated')#url 



class PostingDetailSerializer(serializers.HyperlinkedModelSerializer):
   # author_username = ReadOnlyField(source='author.username')
    class Meta:
        model = Posting
        fields = ('title','id')
    #    fields = ('id','author_username','title','like','content','photo','gps','created','updated')



class CommentSerializer(serializers.ModelSerializer):
    #posting = ReadOnlyField(source='posting')
    #author_username = ReadOnlyField(source='author.username')
    class Meta:
        model = Comment
        fields = ('posting','reply')#('author_username','posting','reply','c_created','c_updated')


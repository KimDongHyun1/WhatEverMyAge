#from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers
from .models import Pictures, Post

class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pictures
        fields = ('picture',)

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('message','title')


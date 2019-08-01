#from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers
from .models import Post,Pictures 

class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pictures
        fields = ('picture','description')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('message','title')


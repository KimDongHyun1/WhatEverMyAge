#from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers
from .models import Pictures

class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pictures
        fields = ('picture',)
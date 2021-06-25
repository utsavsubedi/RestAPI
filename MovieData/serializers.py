from rest_framework import serializers
from .models import MovieInfo


class MovieSerializer(serializers.ModelSerializer):
    image = serializers.ImageField( max_length= None, use_url = True )
    class Meta:
        model = MovieInfo
        fields = ["id","name", "duration", "description", "genre", "image"]


from rest_framework import serializers
from .models import Anime


class AnimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Anime
        fields = ['nombre', 'capitulos', 'temporadas', 'genero', 'sinopsis', 'fecha_emision']
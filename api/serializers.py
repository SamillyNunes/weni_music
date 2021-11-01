from rest_framework import serializers

from .models import MusicModel, ArtistModel, PlaylistModel


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicModel
        fields = ('id', 'title', 'artist')


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistModel
        fields = ('id', 'name')


class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaylistModel
        fields = ('id', 'musics')

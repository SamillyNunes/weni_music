from rest_framework import serializers

from .models import MusicModel, ArtistModel, PlaylistModel


class MusicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MusicModel
        fields = ('id', 'title', 'artist')


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ArtistModel
        fields = ('id', 'name')


class PlaylistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlaylistModel
        fields = ('id', 'musics')

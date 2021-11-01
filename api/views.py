from rest_framework import viewsets

from .serializers import MusicSerializer, ArtistSerializer, PlaylistSerializer
from .models import MusicModel, ArtistModel, PlaylistModel


class MusicViewSet(viewsets.ModelViewSet):
    queryset = MusicModel.objects.all().order_by('title')
    serializer_class = MusicSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = ArtistModel.objects.all().order_by('name')
    serializer_class = ArtistSerializer


class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = PlaylistModel.objects.all()
    serializer_class = PlaylistSerializer

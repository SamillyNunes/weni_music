from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import MusicSerializer, ArtistSerializer, PlaylistSerializer
from .models import MusicModel, ArtistModel, PlaylistModel


class MusicAPIView(APIView):
    """
    API que provê as músicas
    """

    def get(self, request, pk=None):
        # Caso o id não seja nulo, significa que é para retornar apenas a música selecionada
        if pk is not None:
            music = MusicModel.objects.filter(id=pk)
            if not music.exists():
                data = {'error': 'Music selected does not exist'}
                return Response(data=data, status=status.HTTP_404_NOT_FOUND)

            music = MusicModel.objects.get(id=pk)
            serializer = MusicSerializer(music)
            return Response(serializer.data, status=status.HTTP_200_OK)

        musics = MusicModel.objects.all()
        serializer = MusicSerializer(musics, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MusicSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)


class ArtistAPIView(APIView):
    """
    API que provê os artistas
    """

    def get(self, request, pk=None):
        # Caso o id não seja nulo, significa que é para retornar apenas a música selecionada
        if pk is not None:
            artist = ArtistModel.objects.filter(id=pk)
            if not artist.exists():
                data = {'error': 'Artist selected does not exist'}
                return Response(data=data, status=status.HTTP_404_NOT_FOUND)

            artist = ArtistModel.objects.get(id=pk)
            serializer = ArtistSerializer(artist)
            return Response(serializer.data, status=status.HTTP_200_OK)

        artists = ArtistModel.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ArtistSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)


class PlaylistAPIView(APIView):
    """
    API que provê as playlists
    """

    def get(self, request, pk=None):
        # Caso o id não seja nulo, significa que é para retornar apenas a música selecionada
        if pk is not None:
            playlist = PlaylistModel.objects.filter(id=pk)
            if not playlist.exists():
                data = {'error': 'Playlist selected does not exist'}
                return Response(data=data, status=status.HTTP_404_NOT_FOUND)

            playlist = PlaylistModel.objects.get(id=pk)
            serializer = PlaylistSerializer(playlist)
            return Response(serializer.data, status=status.HTTP_200_OK)

        playlists = PlaylistModel.objects.all()
        serializer = PlaylistSerializer(playlists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PlaylistSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

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

    def put(self, request, pk):
        # Pegando a musica pelo id passado pelo endpoint
        music = MusicModel.objects.get(id=pk)

        # Facilitando o acesso aos dados da requisição, atribuindo-os a variavel data
        data = request.data

        if "title" in data.keys():
            music.title = data["title"]
        if "artist" in data.keys():
            # filtrando os artistas que tem o id solicitado
            artist = ArtistModel.objects.filter(id=data["artist"])

            # se existir algum registro, pega esse registro e atualiza
            if artist.exists():
                artist = ArtistModel.objects.get(id=data["artist"])
                music.artist = artist
            # Se nao existir, manda uma requisicao com 404 erro
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)

        # Salvando a instância atualizada
        music.save()
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, pk):
        music = MusicModel.objects.filter(id=pk)

        if music.exists():
            music = MusicModel.objects.get(id=pk)
            music.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


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

    def put(self, request, pk):
        # Pegando o artista pelo id passado pelo endpoint
        artist = ArtistModel.objects.get(id=pk)

        # Facilitando o acesso aos dados da requisição, atribuindo-os a variavel data
        data = request.data

        if "name" in data.keys():
            artist.name = data["name"]

        artist.save()
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, pk):
        artist = ArtistModel.objects.filter(id=pk)

        if artist.exists():
            artist = ArtistModel.objects.get(id=pk)
            artist.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


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

    def put(self, request, pk):
        # Pegando a playlist pelo id passado pelo endpoint
        playlist = PlaylistModel.objects.get(id=pk)
        print("Playlist founded: ", playlist)

        # Facilitando o acesso aos dados da requisição, atribuindo-os a variavel data
        data = request.data

        print("data.keys: ", data.keys())
        if "musics" in data.keys():
            print("hey!")
            print("data[musics]: ", data["musics"])
            playlist.musics.set(data["musics"])

        playlist.save()
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, pk):
        playlist = PlaylistModel.objects.filter(id=pk)

        if playlist.exists():
            playlist = PlaylistModel.objects.get(id=pk)
            playlist.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

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
        """
        Retorna uma música só, a partir de um id especificado (pk = primary key), ou todas as músicas
        """

        # Caso o id não seja nulo, significa que é para retornar apenas a música selecionada já que foi
        # requisitado com um endpoint especifico
        if pk is not None:
            # Filtrando os registros com o id passado
            music = MusicModel.objects.filter(id=pk)

            # Se não houver registros, envia o erro 404 (não encontrado)
            if not music.exists():
                return Response(status=status.HTTP_404_NOT_FOUND)

            # Se houver registros, pega a instância única com o id passado serializa, e retorna
            music = MusicModel.objects.get(id=pk)
            serializer = MusicSerializer(music)
            return Response(serializer.data, status=status.HTTP_200_OK)

        # Se o id for nulo, significa que o que está sendo requisitado são todas as músicas
        musics = MusicModel.objects.all()
        serializer = MusicSerializer(musics, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Envia músicas para a API
        """

        # Serializa (converte de json para objeto) a partir da requisição passada
        serializer = MusicSerializer(data=request.data)

        # Se a serialização for válida, salva e retorna o status 201 (criado)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        # Se a serialização não for válida, retorna o status não aceitável (406)
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

    def put(self, request, pk):
        """
        Atualiza uma música da API a partir de um id no endpoint
        """

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
        """
        Deleta uma música a partir do id passado no endpoint
        """

        # Filtrando os registros pelo id passado
        music = MusicModel.objects.filter(id=pk)

        # Se existir registro, deleta e retorna ok (200)
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
        """
        Retorna um artista só, a partir de um id especificado (pk = primary key), ou todos os artistas
        """

        # Caso o id não seja nulo, significa que é para retornar apenas a música selecionada
        if pk is not None:
            artist = ArtistModel.objects.filter(id=pk)
            if not artist.exists():
                return Response(status=status.HTTP_404_NOT_FOUND)

            artist = ArtistModel.objects.get(id=pk)
            serializer = ArtistSerializer(artist)
            return Response(serializer.data, status=status.HTTP_200_OK)

        artists = ArtistModel.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Envia um artista para o banco de dados
        """

        serializer = ArtistSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

    def put(self, request, pk):
        """
        Atualiza um artista no banco de dados
        """

        # Pegando o artista pelo id passado pelo endpoint
        artist = ArtistModel.objects.get(id=pk)

        # Facilitando o acesso aos dados da requisição, atribuindo-os a variavel data
        data = request.data

        if "name" in data.keys():
            artist.name = data["name"]

        artist.save()
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, pk):
        """
        Deleta um artista do banco de dados
        """

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
        """
        Retorna uma playlist só, a partir de um id especificado (pk = primary key), ou todas as playlists
        """

        # Caso o id não seja nulo, significa que é para retornar apenas a música selecionada
        if pk is not None:
            playlist = PlaylistModel.objects.filter(id=pk)
            if not playlist.exists():
                return Response(status=status.HTTP_404_NOT_FOUND)

            playlist = PlaylistModel.objects.get(id=pk)
            serializer = PlaylistSerializer(playlist)
            return Response(serializer.data, status=status.HTTP_200_OK)

        playlists = PlaylistModel.objects.all()
        serializer = PlaylistSerializer(playlists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Envia uma playlist para o banco de dados
        """

        serializer = PlaylistSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

    def put(self, request, pk):
        """
        Atualiza uma playlist
        """

        # Pegando a playlist pelo id passado pelo endpoint
        playlist = PlaylistModel.objects.get(id=pk)

        # Facilitando o acesso aos dados da requisição, atribuindo-os a variavel data
        data = request.data

        if "musics" in data.keys():
            playlist.musics.set(data["musics"])

        playlist.save()
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, pk):
        """
        Deleta um artista no banco de dados
        """

        playlist = PlaylistModel.objects.filter(id=pk)

        if playlist.exists():
            playlist = PlaylistModel.objects.get(id=pk)
            playlist.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

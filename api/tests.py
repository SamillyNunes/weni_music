from rest_framework.test import APITestCase
from .models import MusicModel, ArtistModel, PlaylistModel


class MusicTest(APITestCase):
    url = '/musics/'

    def setUp(self) -> None:
        """
        Esta função tem por objetivo fazer as configurações iniciais para que os testes executem com sucesso.
        """

        # Criando objetos para os devidos testes
        ArtistModel.objects.create(name='Beyonce')
        MusicModel.objects.create(title='Halo', artist_id=1)

    def test_get(self):
        # Buscando requisição atraves do endpoint
        response = self.client.get(self.url)
        # Transformando a resposta retornada em json
        result = response.json()

        # Testes
        # Comparando o código de status retornado
        self.assertEqual(response.status_code, 200)
        # Comparando o o tipo do conteúdo retornado
        self.assertIsInstance(result, list)
        # Comparando o primeiro elemento
        self.assertEqual(result[0]['title'], 'Halo')

    def test_get_error(self):
        """ Verificando uma possibilidade de erro e se ele é tratado """

        pk = 2

        # Buscando a requisição com um id de música inexistente
        response = self.client.get(self.url + f'{pk}/')

        # Teste: Comparar o código de estado
        self.assertEqual(response.status_code, 404)

    def test_post(self):
        # Criando dados ficticios
        data = {
            'title': 'If I were a boy',
            'artist': '1'
        }

        # Fazendo a requisição post
        response = self.client.post(self.url, data=data)

        # Comparando o código de estado
        self.assertEqual(response.status_code, 201)

    def test_post_error_1(self):
        """ Teste para verificar se vai identificar que o artista 2 nao existe """

        # Criando dados ficticios
        data = {
            'title': 'If I were a boy',
            'artist': '2'
        }

        response = self.client.post(self.url, data=data)

        # Comparando o código de estado
        self.assertEqual(response.status_code, 400)

    def test_post_error_2(self):
        """ Teste para verificar se vai identificar que falta um campo """

        # Dados ficticios faltantes
        data = {
            'title': 'If I were a boy',
        }

        response = self.client.post(self.url, data=data)

        self.assertEqual(response.status_code, 400)

    def test_put(self):
        pk = 1

        data = {
            'title': 'Crazy song',
            'artist': '1'
        }

        response = self.client.put(self.url + f'{pk}/', data=data)

        self.assertEqual(response.status_code, 200)

    def test_put_error(self):
        """ Teste para verificar se vai identificar que o artista 2 nao existe """

        pk = 2

        data = {
            'title': 'Crazy song',
            'artist': '1'
        }

        response = self.client.put(self.url + f'{pk}/', data=data)

        self.assertEqual(response.status_code, 404)

    def test_delete(self):
        pk = 1

        response = self.client.delete(self.url + f'{pk}/')

        self.assertEqual(response.status_code, 200)

    def test_delete_error(self):
        """ Teste para verificar se vai identificar que a música 2 nao existe """
        pk = 2

        response = self.client.delete(self.url + f'{pk}/')

        self.assertEqual(response.status_code, 404)


class ArtistTest(APITestCase):
    url = '/artists/'

    def setUp(self) -> None:
        """
        Esta função tem por objetivo fazer as configurações iniciais para que os testes executem com sucesso.
        """

        # Criando objetos para os devidos testes
        ArtistModel.objects.create(name='Beyonce')

    def test_get(self):
        # Buscando requisição atraves do endpoint
        response = self.client.get(self.url)
        # Transformando a resposta retornada em json
        result = response.json()

        # Testes
        # Comparando o código de status retornado
        self.assertEqual(response.status_code, 200)
        # Comparando o o tipo do conteúdo retornado
        self.assertIsInstance(result, list)
        # Comparando o primeiro elemento
        self.assertEqual(result[0]['name'], 'Beyonce')

    def test_get_error(self):
        """ Verificando uma possibilidade de erro e se ele é tratado """

        pk = 2

        # Buscando a requisição com um id de música inexistente
        response = self.client.get(self.url + f'{pk}/')

        # Teste: Comparar o código de estado
        self.assertEqual(response.status_code, 404)

    def test_post(self):
        # Criando dados ficticios
        data = {
            'name': 'Jay Z',
        }

        # Fazendo a requisição post
        response = self.client.post(self.url, data=data)

        # Comparando o código de estado
        self.assertEqual(response.status_code, 201)

    def test_post_error_2(self):
        """ Teste para verificar se vai identificar que falta um campo """

        # Dados ficticios faltantes
        data = {}

        response = self.client.post(self.url, data=data)

        self.assertEqual(response.status_code, 400)

    def test_put(self):
        pk = 1

        data = {
            'name': 'Bruno Mars',
        }

        response = self.client.put(self.url + f'{pk}/', data=data)

        self.assertEqual(response.status_code, 200)

    def test_put_error(self):
        """ Teste para verificar se vai identificar que o artista 2 nao existe """

        pk = 2

        data = {
            'name': 'Bruno Mars',
        }

        response = self.client.put(self.url + f'{pk}/', data=data)

        self.assertEqual(response.status_code, 404)

    def test_delete(self):
        pk = 1

        response = self.client.delete(self.url + f'{pk}/')

        self.assertEqual(response.status_code, 200)

    def test_delete_error(self):
        """ Teste para verificar se vai identificar que a música 2 nao existe """
        pk = 2

        response = self.client.delete(self.url + f'{pk}/')

        self.assertEqual(response.status_code, 404)


class PlaylistTest(APITestCase):
    url = '/playlists/'

    def setUp(self) -> None:
        """
        Esta função tem por objetivo fazer as configurações iniciais para que os testes executem com sucesso.
        """

        # Criando objetos para os devidos testes
        ArtistModel.objects.create(name='Beyonce')
        MusicModel.objects.create(title='Halo', artist_id=1)
        MusicModel.objects.create(title='If I Were a boy', artist_id=1)
        PlaylistModel.objects.create().musics.set([1, 2])

    def test_get(self):
        # Buscando requisição atraves do endpoint
        response = self.client.get(self.url)
        # Transformando a resposta retornada em json
        result = response.json()

        # Testes
        # Comparando o código de status retornado
        self.assertEqual(response.status_code, 200)
        # Comparando o o tipo do conteúdo retornado
        self.assertIsInstance(result, list)
        # Comparando o primeiro elemento
        self.assertEqual(result[0]['musics'], [1, 2])

    def test_get_error(self):
        """ Verificando uma possibilidade de erro e se ele é tratado """

        pk = 2

        # Buscando a requisição com um id de música inexistente
        response = self.client.get(self.url + f'{pk}/')

        # Teste: Comparar o código de estado
        self.assertEqual(response.status_code, 404)

    def test_post(self):
        # Criando dados ficticios
        data = {
            'musics': [1]
        }

        # Fazendo a requisição post
        response = self.client.post(self.url, data=data)

        # Comparando o código de estado
        self.assertEqual(response.status_code, 201)

    def test_post_error_1(self):
        """ Teste para verificar se vai identificar que a musica 3 nao existe """

        # Criando dados ficticios

        data = {
            'musics': [1, 3]
        }

        response = self.client.post(self.url, data=data)

        # Comparando o código de estado
        self.assertEqual(response.status_code, 400)

    def test_post_error_2(self):
        """ Teste para verificar se vai identificar que falta um campo """

        # Dados ficticios faltantes
        data = {}

        response = self.client.post(self.url, data=data)

        self.assertEqual(response.status_code, 400)

    def test_put(self):
        pk = 1

        data = {
            'musics': [2]
        }

        response = self.client.put(self.url + f'{pk}/', data=data)

        self.assertEqual(response.status_code, 200)

    def test_put_error(self):
        """ Teste para verificar se vai identificar que o artista 2 nao existe """

        pk = 2

        data = {
            'musics': [2]
        }

        response = self.client.put(self.url + f'{pk}/', data=data)

        self.assertEqual(response.status_code, 404)

    def test_delete(self):
        pk = 1

        response = self.client.delete(self.url + f'{pk}/')

        self.assertEqual(response.status_code, 200)

    def test_delete_error(self):
        """ Teste para verificar se vai identificar que a playlist 2 nao existe """
        pk = 2

        response = self.client.delete(self.url + f'{pk}/')

        self.assertEqual(response.status_code, 404)

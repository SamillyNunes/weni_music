from django.urls import path
from django.conf.urls import url
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import MusicAPIView, ArtistAPIView, PlaylistAPIView

schema_view = get_schema_view(
   openapi.Info(
      title="Weni Musics API",
      default_version='v1',
      description="Esta API faz parte do teste técnico para a seleção do estágio da Weni, mais especificamente para o "
                  "cargo de backend com Django. Consiste no serviço de listagem, postagem, atualização e deleção ("
                  "CRUD) de músicas, artistas e playlists. Cada música possui um artista, e cada playlist possui uma "
                  "ou várias músicas",
      contact=openapi.Contact(email="samillynunes19@gmail.com"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('musics/', MusicAPIView.as_view(), name='musics'),
    path('musics/<int:pk>/', MusicAPIView.as_view(), name='musics'),
    path('artists/', ArtistAPIView.as_view(), name='artists'),
    path('artists/<int:pk>/', ArtistAPIView.as_view(), name='artists'),
    path('playlists/', PlaylistAPIView.as_view(), name='playlists'),
    path('playlists/<int:pk>/', PlaylistAPIView.as_view(), name='playlists'),
]
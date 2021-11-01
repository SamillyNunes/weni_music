from django.urls import path, include

from .views import MusicAPIView, ArtistAPIView, PlaylistAPIView

urlpatterns = [
    path('musics/', MusicAPIView.as_view(), name='musics'),
    path('musics/<int:pk>/', MusicAPIView.as_view(), name='musics'),
    path('artists/', ArtistAPIView.as_view(), name='artists'),
    path('artists/<int:pk>/', ArtistAPIView.as_view(), name='artists'),
    path('playlists/', PlaylistAPIView.as_view(), name='playlists'),
    path('playlists/<int:pk>/', PlaylistAPIView.as_view(), name='playlists'),
]
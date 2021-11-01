from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'musics', views.MusicViewSet)
router.register(r'artists',views.ArtistViewSet)
router.register(r'playlists',views.PlaylistViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]
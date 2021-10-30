from django.contrib import admin
from .models import PlaylistModel, MusicModel, ArtistModel

admin.site.register(PlaylistModel)
admin.site.register(MusicModel)
admin.site.register(ArtistModel)

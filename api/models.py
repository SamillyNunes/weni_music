from django.db import models


class ArtistModel(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class MusicModel(models.Model):
    title = models.CharField(max_length=50)
    artist = models.ForeignKey(ArtistModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class PlaylistModel(models.Model):
    musics = models.ManyToManyField(MusicModel)

from django.db import models
from django.contrib.auth import get_user_model


class Song(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название песни')
    artist = models.ForeignKey(
        'Artist', null=True,
        on_delete=models.CASCADE)
    album = models.ForeignKey(
        'Album', null=True,
        on_delete=models.CASCADE)
    genre = models.CharField(max_length=100, blank=True, verbose_name='Жанр')
    duration = models.IntegerField(null=True)
    song_preview = models.CharField(max_length=200, null=True)

    class Meta:
        verbose_name_plural = 'Песни'
        verbose_name = 'Песня'

    def __str__(self):
        return f'{self.name}'


class Artist(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя исполнителя', null=True)
    picture = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'


class Album(models.Model):
    name = models.CharField(max_length=100)
    cover = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'


class Playlist(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название плэйлиста')
    user = models.ForeignKey(
        get_user_model(), null=True,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )

    class Meta:
        verbose_name_plural = 'Плэйлисты'
        verbose_name = 'Плэйлист'

    def __str__(self):
        return f'{self.name}'


class UserSongs(models.Model):
    playlist = models.ForeignKey(
        'Playlist', null=True,
        on_delete=models.CASCADE,
        verbose_name='Плэйлист'
    )
    song = models.ForeignKey(
        'Song', null=True,
        on_delete=models.CASCADE,
        verbose_name='Песня'
    )

    class Meta:
        verbose_name_plural = 'Песни пользователей'
        verbose_name = 'Песня пользователя'
        unique_together = ('playlist', 'song')

    def __str__(self):
        return f'{self.playlist} _ {self.song}'

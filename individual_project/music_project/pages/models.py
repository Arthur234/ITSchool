from django.db import models
from django.contrib.auth import get_user_model


class Song(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название песни')
    artist = models.CharField(max_length=100, verbose_name='Музыкант')
    # musicians = models.ForeignKey
    album = models.CharField(max_length=50, verbose_name='Альбом')
    genre = models.CharField(max_length=100, blank=True, verbose_name='Жанр')
    lyrics = models.TextField(blank=True, null=True, verbose_name='Текст песни')
    tone = models.CharField(max_length=10, verbose_name='Тональность')

    class Meta:
        verbose_name_plural = 'Песни'
        verbose_name = 'Песня'

    def __str__(self):
        return f'{self.pk}: {self.artist} - {self.name}'


class Musicians(models.Model):
    pass


class Playlist(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название плэйлиста')
    user = models.ForeignKey(
        get_user_model(), null=True,
        on_delete=models.PROTECT,
        verbose_name='Пользователь'
    )

    class Meta:
        verbose_name_plural = 'Плэйлисты'
        verbose_name = 'Плэйлист'


class UserSongs(models.Model):

    playlist = models.ForeignKey(
        'Playlist', null=True,
        on_delete=models.PROTECT,
        verbose_name='Плэйлист'
    )
    song = models.ForeignKey(
        'Song', null=True,
        on_delete=models.PROTECT,
        verbose_name='Песня'
    )

    class Meta:
        verbose_name_plural = 'Песни пользователей'
        verbose_name = 'Песня пользователя'
        unique_together = ('playlist', 'song')



from django.contrib import admin

from .models import Song, Playlist, UserSongs, Album, Artist


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('name', 'artist', 'album', 'genre',)
    list_display_links = ('name', 'artist',)
    search_fields = ('name', 'artist',)


admin.site.register([Playlist, UserSongs, Album, Artist])
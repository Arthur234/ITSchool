from django.contrib import admin

from .models import Song, Playlist, UserSongs


class SongAdmin(admin.ModelAdmin):
    list_display = ('name', 'artist', 'album', 'genre',)
    list_display_links = ('name', 'artist',)
    search_fields = ('name', 'artist',)


admin.site.register([Playlist, UserSongs])

admin.site.register(Song, SongAdmin)

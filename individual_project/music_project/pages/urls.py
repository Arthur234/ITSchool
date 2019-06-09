from django.urls import path

from .views import (
    index,
    get_song_detail,
    add_song,
    create_playlist,
    get_playlist,
    get_detailed_playlist,
    search_song,
    delete_playlist,
    delete_song_from_playlist,
)

urlpatterns = [
    path('',  index, name='home'),
    path('^/$', search_song, name='place_search'),

    path('song/<int:song_id>/', get_song_detail, name='song_detail'),
    path('song/<int:song_id>/add/', add_song, name='add_song_in_playlist'),

    path('playlists/create_new/', create_playlist, name='create_playlist'),
    path('playlists/<int:user_id>/', get_playlist, name='playlist'),
    path('playlists/<int:user_id>/detail/<int:playlist_id>/', get_detailed_playlist, name='detailed_playlist'),
    path('playlists/<int:user_id>/detail/<int:playlist_id>/delete/', delete_playlist, name='delete_playlist'),
    path('playlists/<int:user_id>/detail/<int:playlist_id>/<int:song_id>', delete_song_from_playlist,
         name='delete_song'),

]

from django.urls import path

from .views import *

urlpatterns = [
    path('',  index, name='home'),
    path('song/<int:song_id>/', by_song, name='song_detail'),
    path('song/<int:song_id>/add/', add_in_playlist, name='add_song_in_playlist'),
    path('playlists/create_new/', playlist_create_form, name='create_playlist'),
    path('playlists/<int:user_id>/', playlist, name='playlist'),
]

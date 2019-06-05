from django.urls import path

from .views import *

urlpatterns = [
    path('',  index, name='home'),
    path('song/<int:song_id>/', by_song, name='songs'),
    path('playlists/<int:user_id>/', playlist, name='playlist'),
    path('playlists/create_new/', playlist_create_form, name='create_new_playlist'),
    path('add', add_to_playlist)
]

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Song, Playlist, UserSongs
from .forms import PlaylistForm, ChoosePlaylistForm


def index(request):
    songs = Song.objects.all()
    return render(request, 'home.html', {'songs': songs})


def get_song_detail(request, song_id):
    current_song = Song.objects.get(pk=song_id)
    return render(request, 'song/song_detail.html', {'current': current_song})


def get_playlist(request, user_id):
    current_user = request.user
    playlists = Playlist.objects.filter(user=user_id)


    return render(request, 'playlist/playlists_view.html', {'current_user': current_user, 'playlists': playlists,
                                                            'user_id': user_id})


def get_detailed_playlist(request, user_id, playlist_id):
    print(playlist_id)
    playlist = Playlist.objects.get(pk=playlist_id)
    songs = UserSongs.objects.filter(playlist__name=playlist.name)
    return render(request, 'playlist/detailed_playlist.html', {'playlist':playlist, 'songs':songs})


def create_playlist(request):
    if request.method == 'POST':
        form = PlaylistForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            playlist = Playlist(name=name, user=request.user)
            playlist.save()
            return HttpResponseRedirect('/')
    else:
        form = PlaylistForm()
    return render(request, 'playlist/add.html', {'form': form})


def add_song(request, song_id):
    if request.method == 'POST':
        form = ChoosePlaylistForm(request.user, request.POST)
        if form.is_valid():

            playlist = form.cleaned_data['playlist']
            user_song = UserSongs(playlist=playlist, song=Song.objects.get(id=int(song_id)))
            user_song.save()
            return HttpResponseRedirect('/')
    else:
        form = ChoosePlaylistForm(request.user)
        return render(request, 'playlist/add.html', {'form': form})
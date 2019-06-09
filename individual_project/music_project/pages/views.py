import random

from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Song, Playlist, UserSongs, Artist, Album
from .forms import PlaylistForm, ChoosePlaylistForm


def index(request):
    songs = Song.objects.all()
    return render(request, 'home.html', {'songs': songs})


def get_song_detail(request, song_id):
    current_song = Song.objects.get(pk=song_id)
    return render(request, 'song/song_detail.html', {'current': current_song})


def get_playlist(request, user_id):
    playlists = Playlist.objects.filter(user=user_id)

    number_of_songs_in_playlist = dict()
    genre_of_playlist = dict()


    for pl in playlists:
        number_of_songs_in_playlist[pl.id] = UserSongs.objects.filter(playlist__pk=pl.id).count()

        genres = set()
        songs = UserSongs.objects.filter(playlist__pk=pl.id)
        for i in songs:
            genres.add(i.song.genre)
        genre_of_playlist[pl.id] = genres

        duration = 0
        for i in songs:
            duration += i.song.duration

        minutes, seconds = divmod(duration, 60)

    context = {
        'current_user': request.user,
        'playlists': playlists,
        'user_id': user_id,
        'number_of_songs_in_playlist': number_of_songs_in_playlist,
        'genre_of_playlist': genre_of_playlist,
        'min': minutes,
        'sec': seconds,
    }

    return render(request, 'playlist/playlists_view.html', context)


def get_detailed_playlist(request, user_id, playlist_id):
    playlist = Playlist.objects.get(pk=playlist_id)
    songs = UserSongs.objects.filter(playlist__name=playlist.name)
    return render(request, 'playlist/detailed_playlist.html', {'playlist': playlist, 'songs': songs,
                                                               'user_id': user_id})


def delete_song_from_playlist(requsest, user_id, playlist_id, song_id):
    playlist = Playlist.objects.get(pk=playlist_id)
    songs = UserSongs.objects.filter(playlist__name=playlist.name)

    UserSongs.objects.filter(playlist__name=playlist.name).filter(song__pk=song_id).delete()

    return render(requsest, 'playlist/detailed_playlist.html', {
        'user_id': user_id, 'playlist': playlist, 'songs': songs
    })


def update_playlist_name(request, user_id, playlist_id):
    if request.method == 'POST':
        form = PlaylistForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            Playlist.objects.filter(pk=playlist_id).update(name=name)

            return HttpResponseRedirect('../')
    else:
        form = PlaylistForm()
    return render(request, 'playlist/add.html', {'form': form})


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


def delete_playlist(request, user_id, playlist_id):
    Playlist.objects.get(pk=playlist_id).delete()
    playlists = Playlist.objects.filter(user=user_id)

    return render(request, 'playlist/playlists_view.html', {'current_user': request.user, 'playlists': playlists,
                                                            'user_id': user_id})


def search_song(request):
    query = request.GET.get("q")
    if query not in '':
        by_name = Song.objects.filter(Q(name__icontains=query))
        by_album = Song.objects.filter(Q(album__name__icontains=query))
        by_artist = Song.objects.filter(Q(artist__name__icontains=query))
        songs = Song.objects.none()
    else:
        songs = Song.objects.all()
        by_name = Song.objects.none()
        by_album = Song.objects.none()
        by_artist = Song.objects.none()

    return render(request, 'home.html', {'songs': songs, 'by_name': by_name, 'by_album': by_album,
                                         'by_artist': by_artist})


def artist_view(request, artist_id):
    artist = Artist.objects.get(pk=artist_id)
    artist_songs = Song.objects.filter(artist__pk=artist_id)
    return render(request, 'artist/artist_detail.html', {'artist': artist, 'songs': artist_songs})


def alubm_view(request, album_id):
    album = Album.objects.get(pk=album_id)
    album_songs = Song.objects.filter(album__pk=album_id)
    return render(request, 'album/album_detail.html', {'album': album, 'songs': album_songs})

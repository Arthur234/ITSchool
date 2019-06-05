from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Song, UserSongs, Playlist
from .forms import PlaylistForm, ChoosePlaylistForm


# from individual_project.music_project.users.models import CustomUser


def index(request):
    songs = Song.objects.all()
    return render(request, 'home.html', {'songs': songs})


def by_song(request, song_id):
    current_song = Song.objects.get(pk=song_id)
    return render(request, 'song_detail.html', {'current': current_song})


def playlist(request, user_id):
    current_user = request.user
    playlists = Playlist.objects.filter(user=user_id)
    return render(request, 'playlists.html', {'current_user': current_user, 'playlists': playlists})


def add_to_playlist(request, *args):
    # print(request.user.pk)
    print(args)
    return HttpResponseRedirect("../")


# def create_new_playlist(requsest):
#     return render(requsest, 'create_new_playlist.html')


# class PlaylistCreateForm(CreateView):
#     template_name = 'create_new_playlist.html'
#     form_class = PlaylistForm
#     success_url = reverse_lazy('home')
#
#     def save(self, **kwargs):
#         # context = super().get_context_data(**kwargs)
#         # context['playlist'] = Playlist.objects.all()
#         # return context
#         name = form

def playlist_create_form(request):
    if request.method == 'POST':
        form = PlaylistForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            playlist = Playlist(name=name, user=request.user)
            playlist.save()
            pass

            return HttpResponseRedirect('/')

    else:
        form = PlaylistForm()

    return render(request, 'create_new_playlist.html', {'form': form})


def add_song_in_playlist(request):
    form = ChoosePlaylistForm()

    if request.method == 'POST':
        form = ChoosePlaylistForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect('/')

    return render(request, 'create_new_playlist.html', {'form': form})


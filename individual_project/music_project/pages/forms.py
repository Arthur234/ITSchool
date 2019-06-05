from django.forms import Form, ModelForm, ModelChoiceField

from .models import Playlist


class PlaylistForm(ModelForm):
    class Meta:
        model = Playlist
        fields = ('name', )


class ChoosePlaylistForm(Form):
    playlist = ModelChoiceField(queryset=Playlist.objects.all())

import django
from django.forms import Form, ModelForm, ModelChoiceField, Select

from .models import Playlist


class PlaylistForm(ModelForm):
    class Meta:
        model = Playlist
        fields = ('name',)


class ChoosePlaylistForm(Form):

    playlist = ModelChoiceField(queryset=Playlist.objects.all())

    def __init__(self, user, *args, **kwargs):
        super(ChoosePlaylistForm, self).__init__(*args, **kwargs)
        self.fields['playlist'].queryset = Playlist.objects.filter(user=user)

    class Meta:
        model = Playlist

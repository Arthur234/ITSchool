import requests

class Finder:
    def __init__(self):
        pass

    def get_data_by_name(self, name):
        response = requests.get("https://api.deezer.com/search?q=track:'{}'".format(name))
        data = response.json()
        print(data)

    @staticmethod
    def search_data_by_artist_name(name):
        response = requests.get('https://api.deezer.com/search?q=artist:%22{}%22'.format(name))
        data = response.json()

        d = []
        for i in range(len(data['data'])):
            name = data['data'][i]['title']
            artist = data['data'][i]['artist']['name']
            artist_picture = data['data'][i]['artist']['picture']
            duration = data['data'][i]['duration']
            album = data['data'][i]['album']['title']
            album_cover = data['data'][i]['album']['cover']
            song_preview = data['data'][i]['preview']

            album_id = data['data'][i]['album']['id']
            album_data = requests.get('https://api.deezer.com/album/{}/'.format(album_id)).json()
            genre = album_data['genres']['data'][0]['name']

            d.append([name, artist, album, genre, duration, song_preview, artist_picture, album_cover])

        return d

'''
shell script

from pages.controllers.upload_data.get_deezer_data import Finder
from pages.models import Song, Artist, Album 

finder = Finder()
data = finder.search_data_by_artist_name('Земфира')
artist = Artist.objects.get_or_create(name=data[0][1], picture=data[0][6])

for i in data:
    album = Album.objects.get_or_create(name=i[2], cover=i[7])
    Song.objects.create(name=i[0], album=album[0], artist=artist[0], genre=i[3], duration=i[4], song_preview=i[5])
'''

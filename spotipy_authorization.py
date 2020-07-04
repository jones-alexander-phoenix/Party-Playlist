import configparser
import spotipy.util as util
import spotipy
from pprint import pprint

scope = 'user-library-read user-read-currently-playing'

config = configparser.ConfigParser()
config.read('config.cfg')
username = config.get('SPOTIFY', 'USER')
client_id = config.get('SPOTIFY', 'CLIENT_ID')
client_secret = config.get('SPOTIFY', 'CLIENT_SECRET')
redirect_uri = config.get('SPOTIFY', 'SPOTIPY_REDIRECT_URI')

token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
sp = spotipy.Spotify(auth=token)

class Spotipush:
    def __init__(self):
        self.playlist = sp.playlist(playlist_id="3tH62AfZywmIiBhGFHAKzz")
        self.playlist_tracks = sp.playlist_tracks(playlist_id="3tH62AfZywmIiBhGFHAKzz",
                                                  fields='items,uri,name,id,total',
                                                  market='fr')
        self.current_track = sp.current_user_playing_track()

    def get_tracks(self):
        return self.playlist_tracks


spt = Spotipush()

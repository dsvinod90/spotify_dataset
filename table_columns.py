from enum import Enum

class TableColumns(Enum):
    PLAYLIST = ['pid', 'name', 'collaborative', 'duration_ms']
    ARTIST = ['artist_uri', 'artist_name']
    ALBUM = ['album_uri', 'album_name']
    TRACK = ['track_uri', 'track_name', 'album_uri']
    TRACK_PLAYLIST = ['track_uri', 'pid', 'pos']
    TRACK_ARTIST = ['track_uri', 'artist_uri']
    ALBUM_ARTIST = ['album_uri', 'artist_uri']
    PLAYLIST_KEYS = ['pid', 'name', 'collaborative', 'duration_ms']
    TRACK_KEYS = ['pos', 'artist_name', 'track_uri', 'artist_uri', 'track_name', 'album_uri', 'album_name']
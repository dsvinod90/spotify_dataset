from enum import Enum

class TempFiles(Enum):
    PLAYLIST = 'temp/temp_playlist.csv'
    ARTIST = 'temp/temp_artist.csv'
    ALBUM = 'temp/temp_album.csv'
    TRACK = 'temp/temp_track.csv'
    TRACK_PLAYLIST = 'temp/temp_track_playlist.csv'
    TRACK_ARTIST = 'temp/temp_track_artist.csv'
    ALBUM_ARTIST = 'temp/temp_album_artist.csv'
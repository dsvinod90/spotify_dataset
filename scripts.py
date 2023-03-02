from enum import Enum

class Scripts(Enum):
    SCHEMA = 'sql_scripts/create_schema.sql'
    PLAYLIST = 'sql_scripts/populate_playlist.sql'
    ARTIST = 'sql_scripts/populate_artist.sql'
    ALBUM = 'sql_scripts/populate_album.sql'
    TRACK = 'sql_scripts/populate_track.sql'
    TRACK_PLAYLIST = 'sql_scripts/populate_track_playlist.sql'
    TRACK_ARTIST = 'sql_scripts/populate_track_artist.sql'
    ALBUM_ARTIST = 'sql_scripts/populate_album_artist.sql'
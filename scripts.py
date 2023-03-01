from enum import Enum

class Scripts(Enum):
    SCHEMA = 'sql_scripts/create_schema.sql'
    PLAYLIST = 'sql_scripts/populate_playlist.sql'
    ARTIST = 'sql_scripts/populate_artist.sql'
    TRACK = 'sql_scripts/populate_track.sql'
    TRACK_PLAYLIST = 'sql_scripts/populate_track_playlist.sql'
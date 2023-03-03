"""
TableColumns.py
CSCI-620: Project - Phase1

__author__ = "Vinod Dalavai, Samson Zhang, Ramprasad Kokkula"
"""

from enum import Enum

class TableColumns(Enum):
    """Enum for table columns
    """

    PLAYLIST = ['pid', 'name', 'collaborative', 'playlist_duration_ms']
    ARTIST = ['artist_uri', 'artist_name']
    ALBUM = ['album_uri', 'album_name']
    TRACK = ['track_uri', 'track_name', 'album_uri', 'track_duration_ms']
    TRACK_PLAYLIST = ['track_uri', 'pid', 'pos']
    TRACK_ARTIST = ['track_uri', 'artist_uri']
    ALBUM_ARTIST = ['album_uri', 'artist_uri']
    PLAYLIST_KEYS = ['pid', 'name', 'collaborative', 'duration_ms']
    TRACK_KEYS = ['pos', 'artist_name', 'track_uri', 'artist_uri', 'track_name', 'album_uri', 'album_name', 'duration_ms']
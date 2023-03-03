CREATE TABLE IF NOT EXISTS album(
    album_uri CHAR(255),
    name VARCHAR
);

CREATE TABLE IF NOT EXISTS temp_track(
    track_uri CHAR(255),
    name VARCHAR,
    album_uri CHAR(255),
    duration VARCHAR(15)
);

CREATE TABLE IF NOT EXISTS temp_artist(
    artist_uri CHAR(255),
    name VARCHAR
);

CREATE TABLE IF NOT EXISTS temp_playlist(
    playlist_id VARCHAR (10),
    name VARCHAR,
    collab VARCHAR (10),
    duration VARCHAR (15)
);

CREATE TABLE IF NOT EXISTS temp_album_artist(
    album_uri CHAR(255),
    artist_uri CHAR(255)
);

CREATE TABLE IF NOT EXISTS temp_track_artist(
    track_uri CHAR(255),
    artist_uri CHAR(255)
);
 
CREATE TABLE IF NOT EXISTS temp_track_playlist(
    track_uri CHAR(255),
    playlist_id CHAR(20),
    position CHAR(20)
);
CREATE TABLE IF NOT EXISTS album(
    album_uri CHAR(255),
    name VARCHAR
);

CREATE TABLE IF NOT EXISTS track(
    track_uri CHAR(255),
    name VARCHAR,
    album_uri CHAR(255)
);

CREATE TABLE IF NOT EXISTS temp_artist(
    artist_uri CHAR(255),
    name VARCHAR
);

CREATE TABLE IF NOT EXISTS temp_playlist(
    playlistid VARCHAR (10),
    name VARCHAR,
    collab VARCHAR (10),
    duration VARCHAR (10)
);

-- CREATE TABLE IF NOT EXISTS album_artist(
-- album int,
-- artist int,
-- PRIMARY KEY (album, artist),
-- FOREIGN KEY (album) REFERENCES album(albumid),
-- FOREIGN KEY (artist) REFERENCES artist(artistid)
-- );
-- 
-- CREATE TABLE IF NOT EXISTS track_artist(
-- track int,
-- artist int,
-- PRIMARY KEY (track, artist),
-- FOREIGN KEY (track) REFERENCES track(trackid),
-- FOREIGN KEY (artist) REFERENCES artist(artistid)
-- );
-- 
-- CREATE TABLE IF NOT EXISTS track_playlist(
-- track int,
-- playlist int,
-- position int,
-- PRIMARY KEY (track, playlist),
-- FOREIGN KEY (track) REFERENCES track(trackid),
-- FOREIGN KEY (playlist) REFERENCES playlist(playlistid)
-- );
CREATE TABLE album(
albumid int PRIMARY KEY,
uri char(255),
name char(255)
);

CREATE TABLE track(
trackid int PRIMARY KEY,
uri char(255),
name char(255),
duration int,
albumid int,
FOREIGN KEY (albumid) REFERENCES album(albumid)
);

CREATE TABLE artist(
artistid int PRIMARY KEY,
uri char(255),
name char(255)
);

CREATE TABLE playlist(
playlistid int PRIMARY KEY,
collab boolean,
duration int
);

CREATE TABLE album_artist(
album int,
artist int,
PRIMARY KEY (album, artist),
FOREIGN KEY (album) REFERENCES album(albumid),
FOREIGN KEY (artist) REFERENCES artist(artistid)
);

CREATE TABLE track_artist(
track int,
artist int,
PRIMARY KEY (track, artist),
FOREIGN KEY (track) REFERENCES track(trackid),
FOREIGN KEY (artist) REFERENCES artist(artistid)
);

CREATE TABLE track_playlist(
track int,
playlist int,
position int,
PRIMARY KEY (track, playlist),
FOREIGN KEY (track) REFERENCES track(trackid),
FOREIGN KEY (playlist) REFERENCES playlist(playlistid)
);

CREATE TABLE temp_playlist(
pid VARCHAR,
name VARCHAR,
collaborative VARCHAR,
pos VARCHAR,
artist_name VARCHAR,
track_uri VARCHAR,
artist_uri VARCHAR,
track_name VARCHAR,
album_uri VARCHAR,
album_name VARCHAR
);


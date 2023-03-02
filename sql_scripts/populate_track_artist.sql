COPY temp_track_artist
	FROM '/Users/vinoddalavai/LocalDocuments/CSCI620_BigData/Project/temp/temp_track_artist.csv'
	DELIMITER E','
	CSV HEADER;

SELECT DISTINCT temp_track_artist.track_uri, temp_track_artist.artist_uri
INTO track_artist
FROM temp_track_artist;

ALTER TABLE track_artist
ADD PRIMARY KEY(track_uri, artist_uri);

ALTER TABLE track_artist
ADD CONSTRAINT fk_track_uri FOREIGN KEY track_uri REFERENCES track(track_uri)
ADD CONSTRAINT fk_album_uri FOREIGN KEY album_uri REFERENCES album(album_uri)

DROP TABLE temp_track_artist;

COPY temp_album_artist
	FROM '/Users/vinoddalavai/LocalDocuments/CSCI620_BigData/Project/temp/temp_album_artist.csv'
	DELIMITER E','
	CSV HEADER;

SELECT DISTINCT temp_album_artist.album_uri, temp_album_artist.artist_uri
INTO album_artist
FROM temp_album_artist;

ALTER TABLE album_artist
ADD PRIMARY KEY(album_uri, artist_uri);

DROP TABLE temp_album_artist;
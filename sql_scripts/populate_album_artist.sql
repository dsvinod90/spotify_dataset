COPY temp_album_artist
	FROM '/Users/vinoddalavai/LocalDocuments/CSCI620_BigData/Project/temp/temp_album_artist.csv'
	DELIMITER E','
	CSV HEADER;

SELECT DISTINCT temp_album_artist.album_uri, temp_album_artist.artist_uri
INTO album_artist
FROM temp_album_artist;

DROP TABLE temp_album_artist;

ALTER TABLE album_artist
ADD COLUMN album_id INT,
ADD COLUMN artist_id INT;

UPDATE album_artist
SET album_id = temp.album_id,
	artist_id = temp.artist_id
FROM
(SELECT
	album.id as album_id,
	album.album_uri as album_uri,
	artist.id as artist_id,
	artist.artist_uri as artist_uri
FROM
	album
	JOIN album_artist ON album.album_uri = album_artist.album_uri
	JOIN artist ON album_artist.artist_uri = artist.artist_uri) as temp
WHERE album_artist.album_uri = temp.album_uri AND album_artist.artist_uri = temp.artist_uri;

ALTER TABLE album_artist
DROP CONSTRAINT album_artist_pkey,
DROP COLUMN album_uri,
DROP COLUMN artist_uri,
ADD PRIMARY KEY(album_id, artist_id),
ADD CONSTRAINT fk_album_artist_album FOREIGN KEY(album_id) REFERENCES album(id),
ADD CONSTRAINT fk_album_artist_artist FOREIGN KEY(artist_id) REFERENCES artist(id);
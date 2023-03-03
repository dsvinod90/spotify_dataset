COPY temp_track_artist
	FROM '/Users/vinoddalavai/LocalDocuments/CSCI620_BigData/Project/temp/temp_track_artist.csv'
	DELIMITER E','
	CSV HEADER;

SELECT DISTINCT temp_track_artist.track_uri, temp_track_artist.artist_uri
INTO track_artist
FROM temp_track_artist;

DROP TABLE temp_track_artist;

ALTER TABLE track_artist
ADD COLUMN track_id INT,
ADD COLUMN artist_id INT;

UPDATE track_artist
SET track_id = temp.track_id,
	artist_id = temp.artist_id
FROM
(SELECT
	track.id as track_id,
	track.track_uri as track_uri,
	artist.id as artist_id,
	artist.artist_uri as artist_uri
FROM
	track
	JOIN track_artist ON track.track_uri = track_artist.track_uri
	JOIN artist ON track_artist.artist_uri = artist.artist_uri) as temp
WHERE track_artist.track_uri = temp.track_uri AND track_artist.artist_uri = temp.artist_uri;

ALTER TABLE track_artist
DROP COLUMN track_uri,
DROP COLUMN artist_uri,
ADD CONSTRAINT fk_track_artist_track FOREIGN KEY(track_id) REFERENCES track(id),
ADD CONSTRAINT fk_track_artist_artist FOREIGN KEY(artist_id) REFERENCES artist(id);
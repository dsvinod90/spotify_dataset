COPY temp_track
	FROM '/Users/vinoddalavai/LocalDocuments/CSCI620_BigData/Project/temp/temp_track.csv'
	DELIMITER E','
	CSV HEADER;

SELECT DISTINCT temp_track.track_uri, temp_track.name, temp_track.album_uri, temp_track.duration 
INTO track
FROM temp_track;

ALTER TABLE track
ALTER COLUMN duration TYPE INT USING duration::INTEGER,
ADD COLUMN id SERIAL PRIMARY KEY,
ADD COLUMN album_id INT;

UPDATE track
SET album_id = album.id
FROM album
WHERE album.album_uri = track.album_uri;

ALTER TABLE track
ADD CONSTRAINT fk_track_album FOREIGN KEY(album_id) REFERENCES album(id);

DROP TABLE temp_track;
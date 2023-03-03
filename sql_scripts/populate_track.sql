COPY temp_track
	FROM '/Users/vinoddalavai/LocalDocuments/CSCI620_BigData/Project/temp/temp_track.csv'
	DELIMITER E','
	CSV HEADER;

SELECT DISTINCT temp_track.track_uri, temp_track.name, temp_track.album_uri, temp_track.duration 
INTO track
FROM temp_track;

ALTER TABLE track
ALTER COLUMN duration TYPE INT USING duration::INTEGER,
ADD COLUMN id SERIAL PRIMARY KEY;

DROP TABLE temp_track;
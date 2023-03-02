COPY temp_playlist
	FROM '/Users/vinoddalavai/LocalDocuments/CSCI620_BigData/Project/temp/temp_playlist.csv'
	DELIMITER E','
	CSV HEADER;

SELECT DISTINCT temp_playlist.playlist_id, temp_playlist.name, temp_playlist.collab, temp_playlist.duration
INTO playlist
FROM temp_playlist;

ALTER TABLE playlist
ALTER COLUMN playlist_id TYPE INT USING playlist_id::INTEGER,
ALTER COLUMN collab TYPE BOOLEAN USING collab::BOOLEAN,
ALTER COLUMN duration TYPE INT USING duration::INTEGER;

ALTER TABLE playlist
ADD PRIMARY KEY (playlist_id);

DROP TABLE temp_playlist;
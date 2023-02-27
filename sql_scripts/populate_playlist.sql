COPY temp_playlist
	FROM '/Users/vinoddalavai/LocalDocuments/CSCI620_BigData/Project/temp/temp_playlist.csv'
	DELIMITER E','
	CSV HEADER;

SELECT DISTINCT temp_playlist.playlistid, temp_playlist.name, temp_playlist.collab, temp_playlist.duration
INTO playlist
FROM temp_playlist;

ALTER TABLE playlist
ALTER COLUMN playlistid TYPE INT USING playlistid::INTEGER,
ALTER COLUMN collab TYPE BOOLEAN USING collab::BOOLEAN,
ALTER COLUMN duration TYPE INT USING duration::INTEGER;

ALTER TABLE playlist
ADD PRIMARY KEY (playlistid);

DROP TABLE temp_playlist;
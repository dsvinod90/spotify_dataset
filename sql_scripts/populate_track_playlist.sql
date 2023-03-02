COPY track_playlist
	FROM '/Users/vinoddalavai/LocalDocuments/CSCI620_BigData/Project/temp/temp_track_playlist.csv'
	DELIMITER E','
	CSV HEADER;

ALTER TABLE track_playlist
ALTER COLUMN playlist_id TYPE INT USING playlist_id::INTEGER,
ALTER COLUMN position TYPE SMALLINT USING position::SMALLINT;

ALTER TABLE track_playlist
ADD PRIMARY KEY(track_uri, playlist_id, position);

ALTER TABLE track_playlist
ADD CONSTRAINT fk_track_uri FOREIGN KEY track_uri REFERENCES track(track_uri)
ADD CONSTRAINT fk_playlist_id FOREIGN KEY playlist_id REFERENCES playlist(playlist_id)

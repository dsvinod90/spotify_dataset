COPY temp_track_playlist
	FROM '/Users/vinoddalavai/LocalDocuments/CSCI620_BigData/Project/temp/temp_track_playlist.csv'
	DELIMITER E','
	CSV HEADER;

ALTER TABLE temp_track_playlist
ALTER COLUMN playlist_id TYPE INT USING playlist_id::INTEGER,
ALTER COLUMN position TYPE SMALLINT USING position::SMALLINT;

SELECT
	track.id as track_id,
	temp_track_playlist.playlist_id as playlist_id
	temp_track_playlist.position as position
INTO track_playlist
FROM
	track
	JOIN temp_track_playlist ON track.track_uri = temp_track_playlist.track_uri;

ALTER TABLE track_playlist
ADD PRIMARY KEY(track_id, playlist_id, position),
ADD CONSTRAINT fk_track_playlist_track FOREIGN KEY(track_id) REFERENCES track(id),
ADD CONSTRAINT fk_track_playlist_playlist FOREIGN KEY(playlist_id) REFERENCES playlist(playlist_id);

DROP TABLE temp_track_playlist;
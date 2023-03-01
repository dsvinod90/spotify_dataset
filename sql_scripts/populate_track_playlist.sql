COPY track_playlist
	FROM '/Users/vinoddalavai/LocalDocuments/CSCI620_BigData/Project/temp/temp_track_playlist.csv'
	DELIMITER E','
	CSV HEADER;

ALTER TABLE track_playlist
ADD PRIMARY KEY(track, playlist, position);
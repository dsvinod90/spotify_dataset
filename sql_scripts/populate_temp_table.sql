COPY temp_playlist
	FROM '/Users/vinoddalavai/LocalDocuments/CSCI620_BigData/Project/output/mpd.slice.0-999.csv'
	DELIMITER E','
	CSV HEADER;
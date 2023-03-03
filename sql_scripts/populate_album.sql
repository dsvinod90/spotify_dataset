COPY temp_album
	FROM '/Users/vinoddalavai/LocalDocuments/CSCI620_BigData/Project/temp/temp_album.csv'
	DELIMITER E','
	CSV HEADER;

SELECT DISTINCT temp_album.album_uri, temp_album.name
INTO album
FROM temp_album;

ALTER TABLE album
ADD COLUMN id SERIAL PRIMARY KEY;
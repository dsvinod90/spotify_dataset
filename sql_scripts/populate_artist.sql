COPY temp_artist
	FROM '/Users/vinoddalavai/LocalDocuments/CSCI620_BigData/Project/temp/temp_artist.csv'
	DELIMITER E','
	CSV HEADER;

SELECT DISTINCT temp_artist.artist_uri, temp_artist.name
INTO artist
FROM temp_artist;

ALTER TABLE artist
ADD COLUMN id SERIAL PRIMARY KEY;

DROP TABLE temp_artist;
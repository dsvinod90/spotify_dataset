COPY track
	FROM '/Users/vinoddalavai/LocalDocuments/CSCI620_BigData/Project/temp/temp_track.csv'
	DELIMITER E','
	CSV HEADER;

ALTER TABLE track
ADD COLUMN id SERIAL PRIMARY KEY;
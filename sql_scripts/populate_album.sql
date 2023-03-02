COPY album
	FROM '/Users/vinoddalavai/LocalDocuments/CSCI620_BigData/Project/temp/temp_album.csv'
	DELIMITER E','
	CSV HEADER;

ALTER TABLE album
ADD COLUMN id SERIAL PRIMARY KEY;
COPY temp_album
    FROM '/Users/ramprasad/spotify_dataset_project/spotify_dataset/temp/album.csv'
    DELIMITER E','
    CSV HEADER;

SELECT DISTINCT temp_album.album_uri, temp_album.album_name
INTO album
FROM temp_album;

ALTER TABLE album
ADD PRIMARY KEY (album_uri);

DROP TABLE temp_album;

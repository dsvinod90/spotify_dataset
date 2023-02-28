import os
import sys
from typing import List
import psycopg2
import pandas as pd

output_playlist_data = 'output/output_playlist_data.csv'
playlist_columns = ['pid', 'name', 'collaborative', 'duration_ms']
artist_columns = ['artist_uri', 'artist_name']
track_columns = ['track_uri', 'track_name', 'album_uri']
album_columns = ['album_uri','album_name']

class DatabaseInitializer:
    def __init__(self, hostname: str, dbname: str) -> None:
        self.connection = psycopg2.connect(host=hostname, dbname=dbname)
        self.connection.set_session(autocommit=True)
        self.cursor = self.connection.cursor()
        self.data = None
 
    def _execute_script(self, script_path: str) -> None:
        self.cursor.execute(open(script_path, 'r').read())
    
    def _prepare_dataframe(self) -> None:
        self.data = pd.read_csv(output_playlist_data, encoding='ISO-8859-1')
        self.data.drop_duplicates(subset=None, keep="first", inplace=True)

    def _create_temp_csv_file(self, temp_file_path: str, table_columns: List) -> None:
        self.data.to_csv(temp_file_path, columns=table_columns, index=False, header=True)

    def _populate_album_table(self) -> None:
        self._create_temp_csv_file('temp/temp_album.csv', album_columns)
        self._execute_script('sql_scripts/populate_album.sql')
        

    def _populate_playlist_table(self) -> None:
        self._create_temp_csv_file('temp/temp_playlist.csv', playlist_columns)
        self._execute_script('sql_scripts/populate_playlist.sql')
    
    def _populate_artist_table(self) -> None:
        self._create_temp_csv_file('temp/temp_artist.csv', artist_columns)
        self._execute_script('sql_scripts/populate_artist.sql')

    def _populate_track_table(self) -> None:
        self._create_temp_csv_file('temp/temp_track.csv', track_columns)
        self._execute_script('sql_scripts/populate_track.sql')

    def execute(self):
        self._execute_script('sql_scripts/create_schema.sql')
        self._prepare_dataframe()
        self._populate_playlist_table()
        self._populate_artist_table()
        self._populate_track_table()
        self._populate_album_table()
        self._clean_temp_folder()
        
    def _clean_temp_folder(self):
        for file in os.scandir('temp'):
            os.remove(file)


if __name__ == '__main__':
    if len(sys.argv) == 3:
        hostname = sys.argv[1]
        dbname = sys.argv[2]
        db_init = DatabaseInitializer(hostname, dbname)
        db_init.execute()
    else:
        print("invalid input")
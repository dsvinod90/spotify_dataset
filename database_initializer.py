import os
import sys
import psycopg2
import pandas as pd

from typing import List
from scripts import Scripts
from table_columns import TableColumns
from temp_files import TempFiles
from time_logger import TimeLogger

output_playlist_data = 'output/output_playlist_data.csv'

class DatabaseInitializer:
    def __init__(self, hostname: str, dbname: str, user=None, password=None) -> None:
        print('Connecting to database ...')
        try:
            if user and password:
                self.connection = psycopg2.connect(host=hostname, dbname=dbname, user=user, password=password)
            else:
                self.connection = psycopg2.connect(host=hostname, dbname=dbname)
            self.connection.set_session(autocommit=True)
            self.cursor = self.connection.cursor()
            self.timer = TimeLogger()
            self.data = None
        except(Exception, psycopg2.OperationalError) as error:
            print(error)
            sys.exit(1)
        
    def _execute_script(self, script_path: str) -> None:
        try:
            self.cursor.execute(open(script_path, 'r').read())
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
            sys.exit(1)
    
    def _prepare_dataframe(self) -> None:
        self.timer.start()
        self.data = pd.read_csv(output_playlist_data, encoding='ISO-8859-1')
        self.data.drop_duplicates(subset=None, keep="first", inplace=True)
        self.timer.end()

    def _create_temp_csv_file(self, temp_file_path: str, table_columns: List) -> None:
        self.data.to_csv(temp_file_path, columns=table_columns, index=False, header=True)

    def _populate_table(self, input_sql_script: str, required_columns: str, temp_csv_file: str) -> None:
        self.timer.start()
        self._create_temp_csv_file(temp_csv_file, required_columns)
        self._execute_script(input_sql_script)
        os.remove(temp_csv_file)
        self.timer.end()

    def execute(self):
        print('Creating schema ...')
        self._execute_script(Scripts.SCHEMA.value)
        print('Preparing in-memory dataframe ...')
        self._prepare_dataframe()
        print('Populating playlists ...')
        self._populate_table(Scripts.PLAYLIST.value, TableColumns.PLAYLIST.value, TempFiles.PLAYLIST.value)
        print('Populating artists ...')
        self._populate_table(Scripts.ARTIST.value, TableColumns.ARTIST.value, TempFiles.ARTIST.value)
        print('Populating albums ...')
        self._populate_table(Scripts.ALBUM.value, TableColumns.ALBUM.value, TempFiles.ALBUM.value)
        print('Populating tracks ...')
        self._populate_table(Scripts.TRACK.value, TableColumns.TRACK.value, TempFiles.TRACK.value)
        print('Populating track_playlists ...')
        self._populate_table(Scripts.TRACK_PLAYLIST.value, TableColumns.TRACK_PLAYLIST.value, TempFiles.TRACK_PLAYLIST.value)
        print('Populating track_artists ...')
        self._populate_table(Scripts.TRACK_ARTIST.value, TableColumns.TRACK_ARTIST.value, TempFiles.TRACK_ARTIST.value)
        print('Populating album_artists ...')
        self._populate_table(Scripts.ALBUM_ARTIST.value, TableColumns.ALBUM_ARTIST.value, TempFiles.ALBUM_ARTIST.value)


if __name__ == '__main__':
    if len(sys.argv) == 3:
        hostname = sys.argv[1]
        dbname = sys.argv[2]
        db_init = DatabaseInitializer(hostname, dbname)
    elif len(sys.argv) == 5:
        hostname = sys.argv[1]
        dbname = sys.argv[2]
        username = sys.argv[3]
        password = sys.argv[4]
        db_init = DatabaseInitializer(hostname, dbname, username, password)
    db_init.execute()
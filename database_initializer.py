import os
import sys
import psycopg2
import pandas as pd

from typing import List
from scripts import Scripts
from table_columns import TableColumns
from temp_files import TempFiles

output_playlist_data = 'output/output_playlist_data.csv'

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

    def _populate_table(self, input_sql_script: str, required_columns: str, temp_csv_file: str) -> None:
        self._create_temp_csv_file(temp_csv_file, required_columns)
        self._execute_script(input_sql_script)
        os.remove(temp_csv_file)

    def execute(self):
        self._execute_script(Scripts.SCHEMA.value)
        self._prepare_dataframe()
        self._populate_table(Scripts.PLAYLIST.value, TableColumns.PLAYLIST.value, TempFiles.PLAYLIST.value)
        self._populate_table(Scripts.ARTIST.value, TableColumns.ARTIST.value, TempFiles.ARTIST.value)
        self._populate_table(Scripts.TRACK.value, TableColumns.TRACK.value, TempFiles.TRACK.value)
        self._populate_table(Scripts.TRACK_PLAYLIST.value, TableColumns.TRACK_PLAYLIST.value, TempFiles.TRACK_PLAYLIST.value)


if __name__ == '__main__':
    if len(sys.argv) == 3:
        hostname = sys.argv[1]
        dbname = sys.argv[2]
        db_init = DatabaseInitializer(hostname, dbname)
        db_init.execute()
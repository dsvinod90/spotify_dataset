import os
import sys
import json
import pandas as pd

from typing import Dict
from table_columns import TableColumns
from time_logger import TimeLogger


class Converter:
    def __init__(self):
        self.timer = TimeLogger()
        
    def _get_all_playlists(self, input_data_file: str) -> None:
        with open(input_data_file, 'r') as input_file:
            return json.load(input_file)['playlists']

    def _prepare_dataframe(self, input_data: Dict) -> None:
        row_list = []
        for playlist in input_data:
            p_row = {}
            for key in TableColumns.PLAYLIST_KEYS.value:
                if key == 'duration_ms':
                    p_row['playlist_duration_ms'] = playlist[key]
                else:
                    p_row[key] = playlist[key]
            for track in playlist['tracks']:
                t_row = {}
                for key in TableColumns.TRACK_KEYS.value:
                    if key == 'track_uri':
                        t_row[key] = track[key][14:]
                    elif key == 'artist_uri':
                        t_row[key] = track[key][15:]
                    elif key == 'album_uri':
                        t_row[key] = track[key][14:]
                    elif key == 'duration_ms':
                        t_row['track_duration_ms'] = track[key]
                    else:
                        t_row[key] = track[key]
                row_list.append(p_row | t_row)
        playlist_dataframe = pd.DataFrame(row_list)
        return(playlist_dataframe)
    
    def _prepare_csv_file(self, input_data: pd.DataFrame, output_file_name: str, index: int):
        if index == 0:
            input_data.to_csv(output_file_name, header=True, index=False)
        else:
            input_data.to_csv(output_file_name, mode='a', header=False, index=False)
    
    def execute(self, data_input_folder: str) -> None:
        print('Converting json files to csv file ...')
        self.timer.start()
        for index, input_file in enumerate(os.scandir(data_input_folder)):
            input_data = self._get_all_playlists(input_file.path)
            playlist_dataframe = self._prepare_dataframe(input_data)
            self._prepare_csv_file(playlist_dataframe, f"output/output_playlist_data.csv", index)
        self.timer.end()


if __name__ == '__main__':
    if len(sys.argv) == 2:
        input_data_folder = sys.argv[1]
        Converter().execute(input_data_folder)
    else:
        print('Invalid input')